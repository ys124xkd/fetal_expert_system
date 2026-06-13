import pickle
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score



# Load data
data = pd.read_csv('fetal_health.csv')

# Preprocessing
features = data.columns[:10]  # Select the first 10 columns
X = data[features]
y = data['fetal_health']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Model training
model = DecisionTreeClassifier(criterion='entropy',random_state=17)
model.fit(X_train, y_train)

# Model evaluation
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred) * 100

#incorrect_predictions = (y_pred != y_test).sum()

# Save the model and scaler to a file
with open('model.pkl', 'wb') as f:
    pickle.dump((model, scaler, features, accuracy), f)


