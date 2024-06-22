import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
import joblib

# Step 1: Load the dataset
file_path = r'C:\Harsha files\employee_burnout_analysis-AI.xlsx'
df = pd.read_excel('C:\Harsha files\employee_burnout_analysis-AI.xlsx')

# Inspect the first few rows and column names to identify categorical features
print(df.head())
print(df.columns)
print(df.dtypes)

# Step 2: Data preprocessing
# Handle missing values
df = df.dropna()  # For simplicity, drop rows with missing values

# Identify categorical columns by inspecting the data types
categorical_columns = df.select_dtypes(include=['object']).columns.tolist()
print(f"Categorical Columns: {categorical_columns}")

# Encode categorical variables
for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])

# Ensure all other columns are numeric
# This will convert all columns to numeric, setting errors='coerce' will set invalid parsing to NaN
target_column = 'Burn Rate'  # Update 'Burn Rate' with the actual target column name
numeric_columns = df.columns.difference(categorical_columns + [target_column])
df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

# Drop rows with NaN values resulting from invalid conversions
df = df.dropna()

# Convert the continuous target column to categorical
# Define bins and labels for the categorical target
bins = [0, 0.33, 0.66, 1.0]
labels = ['Low', 'Medium', 'High']
df['Burn Rate'] = pd.cut(df['Burn Rate'], bins=bins, labels=labels)

# Encode the new categorical target variable
le_target = LabelEncoder()
df['Burn Rate'] = le_target.fit_transform(df['Burn Rate'])

# Split the data into features (X) and target (y)
X = df.drop('Burn Rate', axis=1)
y = df['Burn Rate']

# Normalize/scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 3: Feature selection (optional, assuming all features are relevant for simplicity)

# Step 4: Model training
# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.3, random_state=42)

# Initialize the model
model = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
model.fit(X_train, y_train)

# Step 5: Model evaluation
# Predict on the test set
y_pred = model.predict(X_test)

# Evaluate the model
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
print("\nAccuracy Score:")
print(accuracy_score(y_test, y_pred))

# Save the model for future use
joblib.dump(model, 'employee_burnout_model.pkl')
