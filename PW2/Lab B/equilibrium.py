"""
PW2 Lab B Part 4 -- chemical equilibrium via the equilibrium constant K.

Reaction  H2 + I2 <=> 2 HI, starting from 1 mol H2 and 1 mol I2.
As the reaction proceeds by an extent x:  H2 = 1-x,  I2 = 1-x,  HI = 2x.
At equilibrium the composition satisfies the equilibrium constant
        K = [HI]^2 / ([H2][I2]) = (2x)^2 / ((1-x)(1-x)).
Given K, find the extent x. Solve it TWO ways and compare.
Run:  python equilibrium.py
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import newton, minimize

K = 15.6
a = b = 1.0

# TODO 1: write k_imbalance(x) = (2x)^2/((a-x)(b-x)) - K.
#         It equals zero exactly at equilibrium.

def k_imbalance(x):
    return (2*x)**2 / ((a - x)*(b - x)) - K

# TODO 2 (method 1): use scipy.optimize.newton to find the root of k_imbalance
#         (start x0=0.5). This is root-finding.

x_newton = newton(k_imbalance, 0.5)
print("Newton:", x_newton)

# TODO 3 (method 2): use scipy.optimize.minimize to minimise k_imbalance(x)**2
#         (method "SLSQP", bounds [(0, 0.999)], x0=[0.5]). Print both answers
#         and confirm they agree.

res = minimize(lambda z: k_imbalance(z[0])**2, [0.5],
               method="SLSQP", bounds=[(0, 0.999)])
x_slsqp = res.x[0]
print("SLSQP: ", x_slsqp)
print("Agree:", np.isclose(x_newton, x_slsqp, atol=1e-3))

# TODO 4: report the equilibrium amounts (H2, I2, HI), and plot how the three
#         amounts change with the extent x, marking the equilibrium. Save
#         equilibrium.png.

x_eq = x_newton
print(f"H2 = {a - x_eq:.3f}, I2 = {b - x_eq:.3f}, HI = {2*x_eq:.3f} mol")

x = np.linspace(0, 0.99, 200)
plt.plot(x, a - x, label="H2")
plt.plot(x, b - x, "--", label="I2")
plt.plot(x, 2*x, label="HI")
plt.axvline(x_eq, color="gray", linestyle=":", label=f"equilibrium x = {x_eq:.3f}")
plt.xlabel("Extent x (mol)")
plt.ylabel("Amount (mol)")
plt.legend()
plt.savefig("equilibrium.png", dpi=150)
plt.show()