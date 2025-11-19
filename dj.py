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

    # Two-condition form:
    # - Control (m) gets Z if target (n) ∈ {C, D}
    # - Target (n) gets X if control (m) ∈ {B, C}
    new_m, new_n = m, n
    if n in ('C', 'D'):
        new_m = Z_symbol(m)
    if m in ('B', 'C'):
        new_n = X_symbol(n)

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

def print_circuit(circuit, ascii_ket=False):
    """
    For 2 wires, output example:

          00        01        02        03        04        05
    [PU] ∣DD⟩ [X1] ∣DC⟩ [H0] ∣BC⟩ [H1] ∣BC⟩ [CX01] ∣CD⟩ [H0] ∣CD⟩
    [PU] ∣00⟩ [X1] ∣01⟩ [H0] ∣11⟩ [H1] ∣11⟩ [CX01] ∣10⟩ [H0] ∣10⟩ : [Balanced]
    """
    # Choose delimiters for ket formatting
    # Always prefer Unicode kets unless explicitly overridden
    if ascii_ket:
        left, right = '|', '>'
    else:
        left, right = '∣', '⟩'

    # Build raw tokens for each step
    step_labels = [f"{step:02d}" for step, _, _, _ in circuit]
    sym_tokens = [f"{gate} {left}{''.join(state)}{right}" for _, gate, state, _ in circuit]
    bit_tokens = [f"{gate} {left}{''.join(str(b) for b in bits)}{right}" for _, gate, _, bits in circuit]

    # Fixed-width layout per spec:
    # - 8-char columns when CX label is "[CX]"
    # - 10-char columns when CX includes indices like "[CX01]"
    has_cx_with_indices = any(gate.startswith('[CX') and len(gate) > 4 for _, gate, _, _ in circuit)
    col_width = 10 if has_cx_with_indices else 8

    # Right-align cells within each column width; headers right-aligned too
    header = " ".join(f"{lbl:>{col_width}}" for lbl in step_labels)
    sym_line = " ".join(f"{tok:>{col_width}}" for tok in sym_tokens)
    bit_line = " ".join(f"{tok:>{col_width}}" for tok in bit_tokens)

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
