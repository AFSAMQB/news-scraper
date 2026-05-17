import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("customer_purchase_dataset.csv")

# Features and target
X = df[["Age", "Income", "Visited_Website"]]
y = df["Purchased"]

# Scale data (VERY IMPORTANT)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.2, random_state=42
)

# Model with higher iterations
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
print("Model Accuracy:", accuracy_score(y_test, y_pred))

# New customer prediction (IMPORTANT FIX)
new_customer = pd.DataFrame([[30, 40000, 1]], columns=["Age", "Income", "Visited_Website"])
new_customer_scaled = scaler.transform(new_customer)

prediction = model.predict(new_customer_scaled)

if prediction[0] == 1:
    print("Customer WILL purchase")
else:
    print("Customer will NOT purchase")