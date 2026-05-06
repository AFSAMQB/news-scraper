import matplotlib.pyplot as plt

import numpy as np

x = np.arange(-10, 11)
y = x**2

plt.figure()
plt.plot(x, y)
plt.title("Line Plot of y = x²")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()