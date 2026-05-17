import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

print("🚀 TITANIC SURVIVAL PREDICTOR STARTING...")

# LOAD DATASET AUTOMATICALLY (NO DOWNLOAD NEEDED!)
df = sns.load_dataset('titanic')
print("✅ Dataset loaded! Shape:", df.shape)
print(df.head())

# QUICK CLEANUP
df['age'].fillna(df['age'].median(), inplace=True)
df['age_group'] = pd.cut(df['age'], bins=[0,12,18,60,100], labels=['Child','Teen','Adult','Senior'])
df['age_group'].fillna('Adult', inplace=True)
df['embarked'].fillna('S', inplace=True)

# ENCODE CATEGORICAL DATA
df['sex'] = df['sex'].map({'male':0, 'female':1})
df['embarked'] = df['embarked'].map({'S':0, 'C':1, 'Q':2})
df['age_group'] = df['age_group'].map({'Child':0, 'Teen':1, 'Adult':2, 'Senior':3})

# SELECT FEATURES
features = ['pclass', 'sex', 'age', 'sibsp', 'parch', 'fare', 'embarked', 'age_group']
X = df[features]
y = df['survived']

# SPLIT DATA
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# TRAIN MODEL
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# TEST MODEL
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f"\n🎯 MODEL ACCURACY: {accuracy:.1%}")

# PREDICT FOR NEW PASSENGER
def predict_survival(pclass, sex, age, sibsp, parch, fare, embarked):
    passenger = np.array([[pclass, 1 if sex=='female' else 0, age, sibsp, parch, fare,
                          0 if embarked=='S' else 1 if embarked=='C' else 2, 2]])
    survival = model.predict(passenger)[0]
    prob = model.predict_proba(passenger)[0][1]
    return "🟢 SURVIVED" if survival==1 else "🔴 DIED", f"{prob:.1%}"

# TEST PREDICTIONS
print("\n📊 TEST PREDICTIONS:")
print(predict_survival(1, 'female', 25, 0, 0, 100, 'S'))  # Rich woman
print(predict_survival(3, 'male', 20, 0, 0, 7, 'S'))     # Poor man
print(predict_survival(2, 'female', 5, 1, 1, 20, 'C'))   # Child with family

print("\n✅ PROGRAM COMPLETE! Your model works!")