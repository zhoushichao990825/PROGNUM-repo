import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import quad

def gauss(x, A, x0, sigma, z0):
    return A * np.exp(-(x-x0)**2 / (2*sigma**2)) + z0

print("--- Gaussian Area Calculator ---")

A = float(input("Enter amplitude (A): "))
x0 = float(input("Enter peak position (x0): "))
sigma = float(input("Enter peak width (sigma): "))
z0 = float(input("Enter y-offset (z0): "))
a = float(input("Enter lower integration limit: "))
b = float(input("Enter upper integration limit: "))
x_vals = np.linspace(x0 - 5*sigma, x0 + 5*sigma, 200)
y_vals = gauss(x_vals, A, x0, sigma, z0)
plt.figure(figsize=(8, 5))
plt.plot(x_vals, y_vals, label="Gaussian curve", color="cyan")
partial_area, _ = quad(gauss, a, b, args=(A, x0, sigma, z0))

x_fill = np.linspace(max(a, x_vals[0]), min(b, x_vals[-1]), 100) 
y_fill = gauss(x_fill, A, x0, sigma, z0)
plt.fill_between(x_fill, y_fill, color="yellow", alpha=0.5, label=f'Shaded Area: {partial_area:.3f}')

print(f"\nThe area under the curve between {a} and {b} is: {partial_area:.5f}")

plt.title("User Supplied Gaussian Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()