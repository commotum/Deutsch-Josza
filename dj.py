import random

# --- Bitwise mapping (symbol -> 0/1) ---

def get_bitwise(symbol):
    mapping = {'A': 0, 'B': 1, 'C': 1, 'D': 0}
    return mapping[symbol]

# --- Single-wire primitive maps on a single symbol ---

def H_symbol(s):
    mapping = {'A': 'A', 'B': 'D', 'C': 'C', 'D': 'B'}
    return mapping[s]

def X_symbol(s):
    mapping = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
    return mapping[s]

def Z_symbol(s):
    mapping = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A'}
    return mapping[s]

# --- Multi-wire gate helpers (operate on the whole state list) ---

def apply_H(state, wire):
    """Apply H to a specific wire index."""
    new_state = state.copy()
    new_state[wire] = H_symbol(new_state[wire])
    gate_label = f"[H{wire}]"
    return gate_label, new_state

def apply_X(state, wire):
    """Apply X to a specific wire index."""
    new_state = state.copy()
    new_state[wire] = X_symbol(new_state[wire])
    gate_label = f"[X{wire}]"
    return gate_label, new_state

def apply_Z(state, wire):
    """Apply Z to a specific wire index."""
    new_state = state.copy()
    new_state[wire] = Z_symbol(new_state[wire])
    gate_label = f"[Z{wire}]"
    return gate_label, new_state

def apply_CX(state, c_wire, t_wire):
    """
    Controlled-X-like two-wire gate using your 4-ary rule:
    control = m, target = n
    """
    new_state = state.copy()
    m = new_state[c_wire]
    n = new_state[t_wire]

    # Your CX rules in (m, n) form
    if m in ('B', 'C') and n in ('C', 'D'):
        new_m, new_n = Z_symbol(m), X_symbol(n)
    elif m in ('B', 'C') and n in ('A', 'B'):
        new_m, new_n = m, X_symbol(n)
    elif m in ('A', 'D') and n in ('C', 'D'):
        new_m, new_n = Z_symbol(m), n
    elif m in ('A', 'D') and n in ('A', 'B'):
        new_m, new_n = m, n
    else:
        raise ValueError(f"Invalid symbols m={m}, n={n}")

    new_state[c_wire] = new_m
    new_state[t_wire] = new_n

    gate_label = f"[CX{c_wire}{t_wire}]"
    return gate_label, new_state

# --- Power-up (initialize all wires) ---

def power_up(num_wires):
    """
    Initialize each wire randomly to A or D.
    Returns:
      circuit (with initial step 0 recorded),
      current_state (list of symbols)
    """
    state = [random.choice(['A', 'D']) for _ in range(num_wires)]
    bits = [get_bitwise(s) for s in state]

    circuit = []
    step = 0
    gate_label = "[PU]"
    circuit.append((step, gate_label, state.copy(), bits.copy()))
    return circuit, state

# --- Circuit bookkeeping ---

def advance(circuit, gate_label, state):
    """
    Append a new step to the circuit, computing bits from state.
    """
    step = len(circuit)  # next step index
    bits = [get_bitwise(s) for s in state]
    circuit.append((step, gate_label, state.copy(), bits))
    return state

# --- Gate dispatcher so we can run arbitrary sequences ---

def apply_gate_spec(state, spec):
    """
    spec is a tuple, e.g.:
      ('PU',)
      ('H', wire)
      ('X', wire)
      ('Z', wire)
      ('CX', c_wire, t_wire)
    Returns (gate_label, new_state).
    """
    op = spec[0]

    if op == 'PU':
        # We'll treat PU as "re-randomize" all wires here if used mid-circuit.
        num_wires = len(state)
        state = [random.choice(['A', 'D']) for _ in range(num_wires)]
        gate_label = "[PU]"
        return gate_label, state

    elif op == 'H':
        _, wire = spec
        return apply_H(state, wire)

    elif op == 'X':
        _, wire = spec
        return apply_X(state, wire)

    elif op == 'Z':
        _, wire = spec
        return apply_Z(state, wire)

    elif op == 'CX':
        _, c_wire, t_wire = spec
        return apply_CX(state, c_wire, t_wire)

    else:
        raise ValueError(f"Unknown gate spec: {spec}")

# --- Pretty-print the circuit ---

def print_circuit(circuit):
    """
    For 2 wires, output example:

          00        01        02        03        04        05
    [PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX01] ∣CD⟩ [H0] ∣CD⟩
    [PU] ∣00⟩ [X1] ∣01⟩ [H0] ∣11⟩ [H1] ∣11⟩ [CX01] ∣10⟩ [H0] ∣10⟩ : [Balanced]
    """
    # Header line with step numbers
    step_labels = [f"{step:02d}" for step, _, _, _ in circuit]
    header = " ".join(f"{lbl:>8}" for lbl in step_labels)

    # Line of symbolic states
    sym_tokens = []
    for _, gate, state, _ in circuit:
        ket = "".join(state)
        token = f"{gate} ∣{ket}⟩"
        sym_tokens.append(f"{token:>8}")
    sym_line = " ".join(sym_tokens)

    # Line of bitwise states
    bit_tokens = []
    for _, gate, _, bits in circuit:
        ket = "".join(str(b) for b in bits)
        token = f"{gate} ∣{ket}⟩"
        bit_tokens.append(f"{token:>8}")
    bit_line = " ".join(bit_tokens)

    # Overall classification from final bits: all same => Constant, else Balanced
    _, _, _, final_bits = circuit[-1]
    balance_type = "Constant" if len(set(final_bits)) == 1 else "Balanced"

    print(header)
    print(sym_line)
    print(f"{bit_line} : [{balance_type}]")


# --- Example: run your original 2-wire circuit in refactored form ---

if __name__ == "__main__":
    num_wires = 2

    # First get initial power-up
    circuit, state = power_up(num_wires)

    # Then specify the rest of the gates *purely as data*:
    gates = [
        ('X', 1),       # X on wire 1
        ('H', 0),       # H on wire 0
        ('H', 1),       # H on wire 1
        ('CX', 0, 1),   # CX(control=0, target=1)
        ('H', 0),       # H on wire 0
    ]

    # Run the gate sequence
    for spec in gates:
        gate_label, state = apply_gate_spec(state, spec)
        advance(circuit, gate_label, state)

    # Print the final circuit trace
    print_circuit(circuit)
