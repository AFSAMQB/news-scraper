import matplotlib.pyplot as plt
import numpy as np


countries = ["USA", "China", "India", "Germany", "Brazil"]
population = [331, 1441, 1393, 83, 213]  # in millions (dummy data)

colors = ["red", "blue", "green", "purple", "orange"]

plt.figure()
plt.bar(countries, population, color=colors)
plt.title("Population of Countries")
plt.xlabel("Countries")
plt.ylabel("Population (millions)")
plt.ylim(0, 1600)  # Proper scaling
plt.show()