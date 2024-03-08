# Diabetes Prediction System using Naive Bayes Classifier

## Overview
This project aims to predict the likelihood of a patient having diabetes based on various parameters such as gender, pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age. The prediction is made using a Naive Bayes classifier.

## Collaborators
- [Muhammed Shebeeb C](https://github.com/cmshebeeb)
- [Nafiya Sherin V](https://github.com/nafya)

## Project Description
This project utilizes machine learning techniques, specifically a Naive Bayes classifier, to predict whether a patient has diabetes or not. It involves data preprocessing, model training, and prediction.

## Dataset
The dataset used for this project contains information about diabetes patients, including their gender, number of pregnancies, glucose level, blood pressure, skin thickness, insulin level, BMI, diabetes pedigree function, and age.
[Diabetes_data.csv](https://github.com/cmshebeeb/Diabetic_Prediction/blob/main/diabetes_data.csv)

## Code Analysis
The Python script `main.py` contains the code for loading the dataset, preprocessing the data, training the Naive Bayes classifier, taking user input for patient information, making predictions, and displaying the results.

### Libraries Used:
- Pandas: For data manipulation and analysis
- Scikit-learn: For machine learning algorithms
- Tabulate: For displaying comparison tables
- matplotlib: For display comparison map and heatmap

## Usage
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Run the `main.py` script.
4. Provide the required patient information when prompted.
5. The model will predict whether the patient has diabetes or not based on the provided information.

## Example
```python
python main.py
Please provide the following information:
Patient Name: Mary Smith
Gender (Male/Female): Female
Pregnancies: 3
Glucose: 180
Blood Pressure: 90
Skin Thickness: 35
Insulin: 200
BMI: 32.5
Diabetes Pedigree Function: 0.7
Age: 45

Normal Range vs. Patient Value:
Parameter                   Normal Range                                                    Patient Value
------------------------  --------------------------------------------------------------  ----------------
Pregnancies                 No established normal range                                      3
Glucose                     Typically below 100 mg/dL                                         180
Blood Pressure              Normal (<120/<80 mmHg)                                            90
Skin Thickness              No established normal range                                       35
Insulin                     No established normal range                                      200
BMI                         Normal (18.5-24.9), Overweight (25-29.9), Obesity (30 or higher)  32.5
Diabetes Pedigree Function  No established normal range                                        0.7
Age                         N/A                                                              45

The model predicts that Mary Smith, Age 45 has diabetes.
