import matplotlib.pyplot as plt
import numpy as np
import random

x_scatter = [random.randint(0, 100) for _ in range(50)]
y_scatter = [random.randint(0, 100) for _ in range(50)]

plt.figure()
plt.scatter(x_scatter, y_scatter, color="blue", marker="o", alpha=0.6)
plt.title("Random Scatter Plot")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.show()