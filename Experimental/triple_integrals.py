
from scipy.integrate import tplquad
from numpy import e

# Define the function to integrate
def f(z, y, x):
    return e**x

# Define the integration bounds
x_lower = 0
x_upper = 1
y_lower = 0
y_upper = lambda x: 1 - x
z_lower = 0 
z_upper = lambda x, y: 1 - x - y

# Calculate the triple integral
result, error = tplquad(f, x_lower, x_upper, y_lower, y_upper, z_lower, z_upper)

print("Result:", result)
print("Error:", error)