# pip install pandas scikit-learn seaborn

import seaborn as sns
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = sns.load_dataset('titanic')

# Keep useful columns
df = df[['survived', 'pclass', 'sex', 'age', 'fare']]

# ✅ Fixed line — no more warning!
df['age'] = df['age'].fillna(df['age'].median())
df = df.dropna()

# Convert text to numbers
le = LabelEncoder()
df['sex'] = le.fit_transform(df['sex'])

# Features and label
X = df[['pclass', 'sex', 'age', 'fare']]
y = df['survived']

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Test model
y_pred = model.predict(X_test)
print(f"Model Accuracy: {accuracy_score(y_test, y_pred) * 100:.2f}%")

# Predict new passenger
# ✅ Use DataFrame so no feature name warning
new_passenger = pd.DataFrame([[3, 1, 22, 7.25]],
                   columns=['pclass', 'sex', 'age', 'fare'])
result = model.predict(new_passenger)
print("Survived!" if result[0] == 1 else "Did Not Survive")