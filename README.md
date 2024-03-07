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
- matplotlib: For diasplay comparission map and heatmap

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
Gender (Male/Female): Female
Pregnancies: 5
Glucose: 120
Blood Pressure: 80
Skin Thickness: 30
Insulin: 150
BMI: 30
Diabetes Pedigree Function: 0.5
Age: 40

Normal Range vs. Patient Value:
Parameter                   Normal Range                                                    Patient Value
------------------------  --------------------------------------------------------------  ----------------
Gender                      N/A                                                             Female
Pregnancies                 No established normal range                                      5
Glucose                     Typically below 100 mg/dL                                         120
Blood Pressure              Normal (<120/<80 mmHg)                                            80
Skin Thickness              No established normal range                                       30
Insulin                     No established normal range                                      150
BMI                         Normal (18.5-24.9), Overweight (25-29.9), Obesity (30 or higher)  30.0
Diabetes Pedigree Function  No established normal range                                        0.5
Age                         N/A                                                              40

The model predicts that the patient does not have diabetes.

