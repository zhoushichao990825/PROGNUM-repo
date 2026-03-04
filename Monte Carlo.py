from numpy import *
import numpy as np
from math import pi

expression = input("function: ")
a = float(input("lower bound: "))
b = float(input("upper bound: "))

x = np.random.uniform(a, b, 100000)
y = eval(expression)
integral = (b - a) * np.mean(y)

print(f"\nThe calculated integral is: {integral}")

# This line prevents the terminal from instantly closing
input("\nPress Enter to exit...")