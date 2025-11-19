import random

def H(n):
    mapping = {'A': 'A', 'B': 'D', 'C': 'C', 'D': 'B'}
    return mapping[n]

def X(n):
    mapping = {'A': 'B', 'B': 'A', 'C': 'D', 'D': 'C'}
    return mapping[n]

def Z(n):
    mapping = {'A': 'D', 'B': 'C', 'C': 'B', 'D': 'A'}
    return mapping[n]

def CX(m, n):
    # Four-region rule
    if m in ('B', 'C') and n in ('C', 'D'):
        return Z(m), X(n)
    elif m in ('B', 'C') and n in ('A', 'B'):
        return m, X(n)
    elif m in ('A', 'D') and n in ('C', 'D'):
        return Z(m), n
    elif m in ('A', 'D') and n in ('A', 'B'):
        return m, n
    else:
        raise ValueError(f"Invalid symbols m={m}, n={n}")

def power_up(m, n):
    # Randomly choose A or D for each wire
    m = random.choice(['A', 'D'])
    n = random.choice(['A', 'D'])
    return m, n

def get_balance(m, n):
    mapping = {'A': 0, 'B': 1, 'C': 1, 'D': 0}
    m_val = mapping[m]
    n_val = mapping[n]
    return m_val, n_val

def print_state(step, m, n):
    m_val, n_val = get_balance(m, n)
    if m_val == n_val:
        balance_type = "Constant"
    else:
        balance_type = "Balanced"
    print(f"Step {step}: (m, n) = ({m}, {n})  ->  balance = ({m_val}, {n_val})  [{balance_type}]")

# --- Circuit evolution ---

state_evolution = []

step = 0
m, n = power_up(None, None)
state_evolution.append((m, n))
print_state(step, m, n)

step += 1
n = X(n)
state_evolution.append((m, n))
print_state(step, m, n)

step += 1
m = H(m)
state_evolution.append((m, n))
print_state(step, m, n)

step += 1
n = H(n)
state_evolution.append((m, n))
print_state(step, m, n)

step += 1
m, n = CX(m, n)
state_evolution.append((m, n))
print_state(step, m, n)

step += 1
m = H(m)
state_evolution.append((m, n))
print_state(step, m, n)

