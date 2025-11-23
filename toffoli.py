import math
from pyquaternion import Quaternion

# ---------------------------------------------------------------------------- #

# Constants

dos = 1 / math.sqrt(2)

# ---------------------------------------------------------------------------- #

# Poles 

poles = [

    Quaternion(1, 0, 0, 0),         # +0
    Quaternion(0, +dos, 0, +dos),   # +0
    Quaternion(-dos, 0, 0, +dos),   # +0
    Quaternion(-dos, -dos, 0, 0),   # +0

    Quaternion(0, 1, 0, 0),         # +1
    Quaternion(-dos, 0, -dos, 0),   # +1
    Quaternion(0, +dos, +dos, 0),   # +1
    Quaternion(-dos, +dos, 0, 0),   # +1

    Quaternion(0, 0, 1, 0),         # -1
    Quaternion(0, -dos, 0, +dos),   # -1
    Quaternion(0, -dos, +dos, 0),   # -1
    Quaternion(0, 0, +dos, -dos),   # -1
    
    Quaternion(0, 0, 0, 1),         # -0
    Quaternion(-dos, 0, +dos, 0),   # -0
    Quaternion(+dos, 0, 0, +dos),   # -0
    Quaternion(0, 0, +dos, +dos),   # -0

]

# ---------------------------------------------------------------------------- #

# Sinqle Qubit Gates

def i_gate() -> Quaternion:
    i_gate = Quaternion(1, 0, 0, 0)
    return i_gate

def x_gate() -> Quaternion:
    x_gate = Quaternion(0, 1, 0, 0)
    return x_gate
    
def y_gate() -> Quaternion:
    y_gate = Quaternion(0, 0, 1, 0)
    return y_gate

def z_gate() -> Quaternion:
    z_gate = Quaternion(0, 0, 0, 1)
    return z_gate

def h_gate() -> Quaternion:
    h_gate = Quaternion(0, dos, 0, dos)
    return h_gate

def p_gate(amplitude: int) -> Quaternion:
    rad = math.radians(amplitude)
    p_gate = Quaternion(math.cos(rad/2), 0, 0, math.sin(rad/2))
    return p_gate

# ---------------------------------------------------------------------------- #