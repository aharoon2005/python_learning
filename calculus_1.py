# Importing library
import sympy as sym

# Declaring variables
x, y, z = sym.symbols('x y z')

# expression of which we have to find derivative
exp = x**3 * y + y**3 + z

# Differentiating exp with respect to x
derivative1_x = sym.diff(exp, x)
print('derivative w.r.t x: ', derivative1_x)

# Differentiating exp with respect to y
derivative1_y = sym.diff(exp, y)
print('derivative w.r.t y: ', 
      derivative1_y)

# Finding second derivative 
# of exp with respect to x
derivative2_x = sym.diff(exp, x, 2)
print('second derivative w.r.t. x: ', 
      derivative2_x)

# Finding second derivative 
# of exp with respect to y
derivative2_y = sym.diff(exp, y, 2)
print('second derivative w.r.t. y: ', 
      derivative2_y)
