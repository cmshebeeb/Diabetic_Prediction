import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.naive_bayes import GaussianNB
from tabulate import tabulate
import matplotlib.pyplot as plt

def predict_diabetes(data_path, use_feature_names=False):
    # Load the dataset
    data = pd.read_csv(data_path)

    # Drop rows with missing target values
    data = data.dropna(subset=['Outcome'])

    # Preprocessing
    label_encoder = LabelEncoder()
    data['Gender'] = label_encoder.fit_transform(data['Gender'])

    # Split features and target variable
    X = data.drop('Outcome', axis=1)
    y = data['Outcome']

    # Build Naive Bayes classifier
    model = GaussianNB()

    if use_feature_names:
        feature_names = ["Gender", "Pregnancies", "Glucose", "Blood Pressure", "Skin Thickness",
                         "Insulin", "BMI", "Diabetes Pedigree Function", "Age"]
        X.columns = feature_names
    else:
        X.columns = None

    model.fit(X, y)

    def get_user_input(prompt):
        return input(prompt)

    def convert_to_numeric(value, prompt):
        try:
            return int(value)
        except ValueError:
            print(f"Invalid input for {prompt}. Please enter a number.")
            return convert_to_numeric(get_user_input(prompt), prompt)

    def convert_to_float(value, prompt):
        try:
            return float(value)
        except ValueError:
            print(f"Invalid input for {prompt}. Please enter a number.")
            return convert_to_float(get_user_input(prompt), prompt)

    # Get user input with units
    print("Please provide the following information:")
    patient_name = get_user_input("Patient Name: ")
    gender = label_encoder.transform([get_user_input("Gender (Male/Female): ")])[0]
    pregnancies = convert_to_numeric(get_user_input("Pregnancies (times): "), "pregnancies")
    glucose = convert_to_numeric(get_user_input("Glucose (mg/dL): "), "glucose")
    blood_pressure = convert_to_numeric(get_user_input("Blood Pressure (mmHg): "), "blood pressure")
    skin_thickness = convert_to_numeric(get_user_input("Skin Thickness (mm): "), "skin thickness")
    insulin = convert_to_numeric(get_user_input("Insulin (μIU/mL): "), "insulin")
    bmi = convert_to_float(get_user_input("BMI (kg/m^2): "), "BMI")
    diabetes_pedigree_function = convert_to_float(get_user_input("Diabetes Pedigree Function: "), "diabetes pedigree function")
    age = convert_to_numeric(get_user_input("Age (years): "), "age")

    # Prepare data for tabulate, excluding Gender
    table_data = [
        ["Pregnancies", "No established normal range", pregnancies],
        ["Glucose", "Typically below 100 mg/dL", glucose],
        ["Blood Pressure", "Normal (<120/<80 mmHg)", blood_pressure],
        ["Skin Thickness", "No established normal range", skin_thickness],
        ["Insulin", "No established normal range", insulin],
        ["BMI", "Normal (18.5-24.9), Overweight (25-29.9), Obesity (30 or higher)", bmi],
        ["Diabetes Pedigree Function", "No established normal range", diabetes_pedigree_function],
        ["Age", "N/A", age]
    ]

    # Display comparison table using tabulate
    print("\nNormal Range vs. Patient Value:")
    print(tabulate(table_data, headers=['Parameter', 'Normal Range', 'Patient Value'], tablefmt='simple'))

    # Ask user if they want to see the comparison chart
    show_chart = get_user_input("Do you want to see the comparison chart? (yes/no): ")
    if show_chart.lower() == 'yes':
        # Plot comparison chart corrected to avoid TypeError
        def plot_comparison_chart(data, patient_name, age):
            parameters = [row[0] for row in data]
            patient_values = [row[2] for row in data]
            normal_range_values = [1 if row[2] == 1 else 0 for row in data] # Assuming 1 for normal, 0 for not normal

            plt.bar(parameters, patient_values, color='blue', label='Patient Value')
            plt.bar(parameters, normal_range_values, color='red', label='Normal Range')
            plt.xlabel('Parameters')
            plt.ylabel('Value')
            plt.title(f"{patient_name}, Age {age}: Comparison of Patient Values to Normal Ranges")
            plt.legend()
            plt.show()

        # Plot the comparison chart after displaying the table
        plot_comparison_chart(table_data, patient_name, age)

    # Make prediction
    if use_feature_names:
        new_data = [gender, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
        new_data_df = pd.DataFrame([new_data], columns=feature_names)
        prediction = model.predict(new_data_df)
    else:
        prediction = model.predict([[gender, pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]])

    # Print prediction
    if prediction[0] == 1:
        print(f"{patient_name}, Age {age}: The model predicts that the patient has diabetes.")
    else:
        print(f"{patient_name}, Age {age}: The model predicts that the patient does not have diabetes.")

# Example usage
predict_diabetes('diabetes_data.csv', use_feature_names=True)
