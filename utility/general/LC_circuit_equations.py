import numpy as np

"""
LC circuit equations:
    f - Frequency [Hz]
    L - Inductance [H]
    C - Capacitance [C]
"""

def L_circuit(f, C):
    L = 1/(((2*np.pi*f) ** 2) * C)
    return L

def f_circuit(C, L):
    f = 1/(2*np.pi*np.sqrt(L*C)) / 1e6
    return f

def C_circuit(f, L):
    C = 1/((2*np.pi*f) ** 2 * L)
    return C


"""
Coil inductance equations:
    L - Inductance (H)
    l - Length (m)
    N - Number of turns
    r - Coil radius (m)
"""

def N_coil(L, r, l):
    mu0 = 4*np.pi*1e-7
    A = np.pi*r**2

    N = np.sqrt((l*L) / (mu0*A))
    return N

def L_coil(r, N, l):
    mu0 = 4 * np.pi * 1e-7
    A = np.pi * r ** 2

    L = mu0 * ((N**2) * A) / l
    return L


"""
Matching capacitor equation:
    Z - Impedence to match (Ohm)
    f - Frequency (Hz)
"""
def matching_cap_simple(Z, f):
    return 1/(2*np.pi*f*Z)


def RLC_impedance(R, L, C, f):
    omega = 2*np.pi*f
    Xc = 1/(omega * C)
    Xl = omega*L

    diff = (1/Xc) - (1/Xl)

    Z = 1/np.sqrt((1/R)**2 + (diff**2))

    return Z

# Capacitances [F]
Cmin = 1e-12
Cmax = 120e-12
C_coax = 85e-12

C_tune_min = Cmin + C_coax
C_tune_max = Cmax + C_coax

print("----- CAPACITANCE -----")
print(f"Tuning capacitor minimum = {Cmin/1e-12}pF")
print(f"Tuning capacitor maximum = {Cmax/1e-12}pF")
print(f"Coax. capacitance = {C_coax/1e-12}pF")
print(f"Tuning capacitor range = {C_tune_min/1e-12}pF - {C_tune_max/1e-12:.2f}pF")
print()

# Resonant frequency [Hz]
f0 = 213e6

# Inductance [H]
Lmin = L_circuit(f0, C_tune_max)
Lmax = L_circuit(f0, C_tune_min)

print("----- INDUCTANCE -----")
print(f"Resonant frequency = {f0/1e6}MHz")
print(f"Minimum L = {Lmin/1e-6:.4f}uH")
print(f"Maximum L = {Lmax/1e-6:.4f}uH")
print()

r = 2.5e-3
length = 10e-3

Nmin = N_coil(Lmin, r, length)
Nmax = N_coil(Lmax, r, length)

print('Required N range: {:.3} turns to {:.3} turns'.format(Nmin, Nmax))

C_matching = matching_cap_simple(49.5, f0)
print(f"Matching capacitance for f = {f0/1e6} MHz, C = {C_matching/1e-12} pF")

