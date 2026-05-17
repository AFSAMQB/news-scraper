import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

df = pd.read_csv('Titanic.csv')

# Correct mapping syntax
df['Sex'] = df['Sex'].map({'male': 0, 'female': 1})

# Fill missing Age values
df['Age'] = df['Age'].fillna(df['Age'].mean())

X = df[['Pclass', 'Sex', 'Age']]
y = df['Survived']

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LogisticRegression()
model.fit(X_train, y_train)

# Predict on test data
prediction = model.predict(X_test)

# Compare test labels with test predictions
print(f"Accuracy: {accuracy_score(y_test, prediction)}")