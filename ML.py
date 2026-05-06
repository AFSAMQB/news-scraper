from scipy.stats import linregress
import matplotlib.pyplot as plt

# Training data (Overs 1–10)
overs = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
scores = [6, 15, 28, 40, 55, 70, 85, 100, 120, 140]

# Linear regression
slope, intercept, r, p, std_err = linregress(overs, scores)

# Prediction function
def predict_score(over):
    return slope * over + intercept

# User input
over_input = float(input("Enter number of overs: "))
predicted_score = predict_score(over_input)

print("Predicted score at", over_input, "overs:", int(predicted_score))

# Regression line
regression_line = []
for x in overs:
    regression_line.append(slope * x + intercept)

# Plot
plt.scatter(overs, scores)
plt.plot(overs, regression_line)

# Mark prediction point
plt.scatter(over_input, predicted_score)

plt.xlabel("Overs")
plt.ylabel("Score")
plt.title("Cricket Score Prediction using Linear Regression")

plt.show()

