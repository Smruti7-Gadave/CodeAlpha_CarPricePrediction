import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import r2_score, mean_absolute_error

# =========================
# LOAD DATA
# =========================
df = pd.read_csv("car data.csv")

print("First 5 rows:\n", df.head())
print("\nColumns:\n", df.columns)

# =========================
# DATA CLEANING
# =========================
df = df.dropna()

# =========================
# FEATURE ENGINEERING
# =========================
df['Car_Age'] = 2026 - df['Year']
df = df.drop(['Car_Name', 'Year'], axis=1)

# =========================
# ENCODING (FIXED)
# =========================
df['Fuel_Type'] = df['Fuel_Type'].map({'Petrol':0, 'Diesel':1, 'CNG':2})
df['Selling_type'] = df['Selling_type'].map({'Dealer':0, 'Individual':1})
df['Transmission'] = df['Transmission'].map({'Manual':0, 'Automatic':1})

# =========================
# REMOVE NOISE
# =========================
df = df[df['Driven_kms'] < 300000]

# =========================
# FEATURES & TARGET
# =========================
X = df[['Present_Price', 'Driven_kms', 'Car_Age', 'Fuel_Type', 'Transmission']]
y = df['Selling_Price']

# =========================
# SPLIT DATA
# =========================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =========================
# TRAIN MODEL
# =========================
model = RandomForestRegressor(
    n_estimators=200,
    max_depth=10,
    random_state=42
)

model.fit(X_train, y_train)

# =========================
# PREDICTION
# =========================
y_pred = model.predict(X_test)

# =========================
# EVALUATION
# =========================
r2 = r2_score(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)

print("\nModel Performance:")
print("Accuracy (R2): {:.2f}%".format(r2 * 100))
print("MAE:", mae)

# =========================
# SAMPLE PREDICTIONS
# =========================
print("\nSample Predictions:")
for i in range(5):
    print("Actual:", y_test.iloc[i], "Predicted:", round(y_pred[i], 2))

# =========================
# VISUALIZATION 1
# =========================
plt.scatter(y_test, y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Price")
plt.show()

# =========================
# VISUALIZATION 2
# =========================
importance = model.feature_importances_

plt.barh(X.columns, importance)
plt.xlabel("Importance")
plt.title("Feature Importance")
plt.show()

# =========================
# 🔥 MANUAL INPUT PREDICTION
# =========================
print("\n--- Predict Car Price Manually ---")

present_price = float(input("Enter Present Price: "))
driven_kms = float(input("Enter Driven KMs: "))
car_age = float(input("Enter Car Age: "))

fuel = input("Fuel Type (Petrol/Diesel/CNG): ")
if fuel == "Petrol":
    fuel = 0
elif fuel == "Diesel":
    fuel = 1
else:
    fuel = 2

transmission = input("Transmission (Manual/Automatic): ")
if transmission == "Manual":
    transmission = 0
else:
    transmission = 1

# FIX: Use DataFrame to avoid warning
input_data = pd.DataFrame(
    [[present_price, driven_kms, car_age, fuel, transmission]],
    columns=['Present_Price', 'Driven_kms', 'Car_Age', 'Fuel_Type', 'Transmission']
)

predicted_price = model.predict(input_data)

print("\n💰 Predicted Selling Price:", round(predicted_price[0], 2))