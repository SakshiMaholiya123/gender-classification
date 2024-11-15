import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle


data = pd.read_csv('gender_classification.csv')


X = data.drop(columns=['gender'])
y = data['gender'].map({'Male': 1, 'Female': 0})  


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)


with open('gender_classification_model.pkl', 'wb') as file:
    pickle.dump(model, file)

print("Model trained and saved as 'gender_classification_model.pkl'")
