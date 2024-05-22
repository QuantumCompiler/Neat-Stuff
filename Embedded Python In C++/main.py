import numpy as np
import matplotlib.pyplot as plt

# Define the x range (0 to 2*pi with 100 points)
x = np.linspace(0, 2 * np.pi, 100)

# Compute the sine of each x point
y = np.sin(x)

# Create the plot
plt.figure()
plt.plot(x, y)  # Plot the sine of each x point

# Labeling the axes
plt.xlabel('x')
plt.ylabel('sin(x)')

# Title of the plot
plt.title('Plot of the Sine Function')

# Show the plot
plt.show()

# print("Hello, World! From Python!")