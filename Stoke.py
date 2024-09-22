import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
from sklearn.preprocessing import LabelEncoder, StandardScaler

# Load the dataset (ensure you have a proper CSV file format)
data = pd.read_csv(r"C:/Users/Gaurav/OneDrive/Desktop/patient-data1.csv")  # Replace with your dataset file path
data.columns = data.columns.str.strip()  # Clean column names

# Data preprocessing
label_encoder = LabelEncoder()
data['medical history'] = label_encoder.fit_transform(data['medical history'])
data['Stroke History'] = label_encoder.fit_transform(data['Stroke History'])
data['Smoking Status'] = label_encoder.fit_transform(data['Smoking Status'])
data['Diabetes Status'] = label_encoder.fit_transform(data['Diabetes Status'])

# Feature Scaling
scaler = StandardScaler()
data[['blood pressure', 'cholesterol']] = scaler.fit_transform(data[['blood pressure', 'cholesterol']])

# Defining features (X) and dynamic target (y)
X = data.copy()
y = (data['age'] > 60) | (data['blood pressure'] > 140) | (data['cholesterol'] > 240)
y = y.astype(int)

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Predictions
y_pred = rf_model.predict(X_test)

# Evaluate the model with zero_division to handle errors
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred)
class_report = classification_report(y_test, y_pred, zero_division=1)

# Print the results
print(f"Accuracy: {accuracy}")
print("Confusion Matrix:")
print(conf_matrix)
print("Classification Report:")
print(class_report)

# Feature importance
importances = rf_model.feature_importances_
feature_names = X.columns
importance_df = pd.DataFrame({'Feature': feature_names, 'Importance': importances})
importance_df = importance_df.sort_values(by='Importance', ascending=False)
print("\nFeature Importance:")
print(importance_df)

# Save predictions to CSV with a new name
data['Predicted_at_risk'] = rf_model.predict(X)
data.to_csv(r"C:/Users/Gaurav/OneDrive/Desktop/patient-data-updated-new.csv", index=False)

print("The dataset with predictions has been saved as 'patient-data-updated-new.csv'.")
