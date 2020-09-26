import matplotlib.pyplot as plt
import numpy as np
from Equation import Expression

# Create the vectors X and Y
x = np.array(range(10))
input_equations = ['1/x']
for equation in input_equations:
    fn = Expression(equation, ["x"])
    y = fn(x)
    plt.plot(x, y)

# Add X and y Label
plt.xlabel('x axis')
plt.ylabel('y axis')

# Add a grid
plt.grid(alpha=.4, linestyle='--')

# Show the plot
plt.show()
