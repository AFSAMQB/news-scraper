import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)

y_sin = np.sin(x)
y_cos = np.cos(x)

plt.figure(figsize=(10, 4))

# Left subplot
plt.subplot(1, 2, 1)
plt.plot(x, y_sin)
plt.title("y = sin(x)")

# Right subplot
plt.subplot(1, 2, 2)
plt.plot(x, y_cos)
plt.title("y = cos(x)")

plt.suptitle("Sine and Cosine Functions")
plt.show()