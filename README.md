# CodeAlpha_CarPricePrediction
CodeAlpha Internship Project - Car Price Prediction using Machine Learning
# 🚗 Car Price Prediction - CodeAlpha

This project is developed as part of the CodeAlpha Internship.  
It uses Machine Learning techniques to predict the selling price of cars based on various features.

## 📌 Project Overview
The goal of this project is to build a regression model that can estimate car prices using features such as:
- Present Price  
- Driven Kilometers  
- Fuel Type  
- Transmission  
- Car Age  

## ⚙️ Features
- Data preprocessing and cleaning  
- Feature engineering (Car Age calculation)  
- Encoding of categorical variables  
- Regression model using Random Forest  
- Model evaluation using R² score and MAE  
- Visualization of predictions and feature importance  
- Manual input prediction for real-time results
- 
## 🧠 Technologies Used
- Python  
- Pandas  
- Scikit-learn  
- Matplotlib  

## 📂 Dataset
The dataset used contains the following columns:
- Car Name  
- Year  
- Selling Price  
- Present Price  
- Driven Kilometers  
- Fuel Type  
- Selling Type  
- Transmission  
- Owner  

## 🚀 How to Run

1. Install required libraries:
2. pip install pandas scikit-learn matplotlib
2. Make sure dataset file is in the same folder:
car data.csv
3. Run the program:
python Car_Price_Prediction.py

## 📊 Model Used
- Random Forest Regressor
##outptut
PS C:\Users\VICTUS\Desktop\code alpha> python Car_Price_Prediction.py
First 5 rows:
   Car_Name  Year  Selling_Price  Present_Price  ...  Fuel_Type Selling_type Transmission Owner
0     ritz  2014           3.35           5.59  ...     Petrol       Dealer       Manual     0
1      sx4  2013           4.75           9.54  ...     Diesel       Dealer       Manual     0
2     ciaz  2017           7.25           9.85  ...     Petrol       Dealer       Manual     0
3  wagon r  2011           2.85           4.15  ...     Petrol       Dealer       Manual     0
4    swift  2014           4.60           6.87  ...     Diesel       Dealer       Manual     0

[5 rows x 9 columns]

Columns:
 Index(['Car_Name', 'Year', 'Selling_Price', 'Present_Price', 'Driven_kms',
       'Fuel_Type', 'Selling_type', 'Transmission', 'Owner'],
      dtype='str')

Model Performance:
Accuracy (R2): 96.22%
MAE: 0.6485288305016756

Sample Predictions:
Actual: 2.75 Predicted: 3.35
Actual: 8.35 Predicted: 8.15
Actual: 0.5 Predicted: 0.49
Actual: 7.45 Predicted: 7.11
Actual: 5.5 Predicted: 5.14
--- Predict Car Price Manually ---
Enter Present Price: 3.35
Enter Driven KMs: 23
Enter Car Age: 2
Fuel Type (Petrol/Diesel/CNG): petrol
Transmission (Manual/Automatic): manual

Predicted Selling Price: 2.12
