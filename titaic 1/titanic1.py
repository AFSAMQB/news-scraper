import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

# ── Step 1: Load YOUR CSV file ─────────────────────────
df = pd.read_csv('Titanic-Dataset.csv')
print("Dataset loaded! Shape:", df.shape)
print(df.head())

# ── Step 2: Keep only useful columns ──────────────────
df = df[['Survived', 'Pclass', 'Sex', 'Age', 'Fare']]

# ── Step 3: Fix missing Age values ────────────────────
df['Age'] = df['Age'].fillna(df['Age'].median())
df = df.dropna()

# ── Step 4: Convert male/female to numbers ────────────
le = LabelEncoder()
df['Sex'] = le.fit_transform(df['Sex'])
# female = 0 , male = 1

# ── Step 5: Input (X) and Output (y) ──────────────────
X = df[['Pclass', 'Sex', 'Age', 'Fare']]
y = df['Survived']

# ── Step 6: Split — 80% Train, 20% Test ───────────────
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ── Step 7: Train the Model ───────────────────────────
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# ── Step 8: Check Accuracy ────────────────────────────
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

# ── Step 9: Predict a New Passenger ──────────────────
new_passenger = pd.DataFrame(
    [[3, 1, 22, 7.25]],
    columns=['Pclass', 'Sex', 'Age', 'Fare']
)
result = model.predict(new_passenger)
print("Result:", "Survived! ✅" if result[0] == 1 else "Did Not Survive ❌")