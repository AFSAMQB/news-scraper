import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

# ---------------------------
# Training Data (Overs vs Score)
# ---------------------------
overs = np.array([1, 3, 5, 7, 10, 12, 15, 18])
scores = np.array([6, 20, 38, 55, 80, 95, 130, 155])

# ---------------------------
# Apply Linear Regression
# ---------------------------
slope, intercept, r, p, std_err = stats.linregress(overs, scores)

# Function for prediction
def predict_score(over):
    return slope * over + intercept

# ---------------------------
# Predict Score for 18 overs
# ---------------------------
predicted = predict_score(18)
print("Predicted Score at 18 overs:", predicted)

# ---------------------------
# Plot Graph
# ---------------------------
plt.scatter(overs, scores, label="Actual Data")       # Data points
plt.plot(overs, predict_score(overs), label="Regression Line")  # Best fit line

plt.title("Predicted Cricket Score based on Overs (Linear Regression)")
plt.xlabel("Overs")
plt.ylabel("Score")

plt.legend()
plt.grid(True)

plt.show()