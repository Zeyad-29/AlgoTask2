from flask import Flask,render_template,request,redirect,url_for
import json
from datetime import datetime

app = Flask(__name__)
json_number_of_patients_path = "number_of_patients.json"
json_patients_path = "patients.json"



# Function to get and update patient count
def get_and_increment_patient_count(month_year):
    try:
        # Load the JSON file
        with open(json_number_of_patients_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, initialize with an empty dict
        data = {}

    # Check if the month exists in the JSON data
    if month_year in data:
        data[month_year] += 1  # Increment the number of patients
    else:
        data[month_year] = 1  # Add the month with a starting count of 1

    # Save the updated data back to the JSON file
    with open(json_number_of_patients_path, "w") as file:
        json.dump(data, file, indent=4)

    return data[month_year]


# Function to add a new patient
def add_patient_to_json(name, age, gender,id):
    try:
        # Load the JSON file
        with open(json_patients_path, "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is empty, initialize with an empty list
        data = {"patients": []}


    # Add the new patient details
    new_patient = {
        "id": id,
        "name": name,
        "age": age,
        "gender": gender
    }
    data["patients"].append(new_patient)

    # Save the updated data back to the JSON file
    with open(json_patients_path, "w") as file:
        json.dump(data, file, indent=4)

    return new_patient

@app.route('/', methods=['GET','POST'])
def add_patient():
    message=''
    with open(json_patients_path, 'r') as f:
        data = json.load(f)
    if (request.method=='POST'):
        patient_name = request.form['name']
        patient_age = request.form['age']
        patient_gender = request.form['gender']
        if patient_name and patient_age and patient_gender:
            # Generate patient ID based on the current month and year
            current_date = datetime.now()
            month_year = f"{current_date.year}-{current_date.month:02d}"
            patient_id = int(f"{current_date.year%100}{current_date.month:02d}")*100000
            patient_id = str(patient_id+int(get_and_increment_patient_count(month_year)))
            add_patient_to_json(patient_name,patient_age,patient_gender,patient_id)
            # Redirect to the same page with success message in query parameters
            return redirect(url_for('add_patient', message=f"Patient added successfully [ID: {patient_id}]"))
        else:
            # Redirect with an error message in query parameters
            return redirect(url_for('add_patient', message="Please enter the data correctly"))

    # Retrieve the optional message from the query string
    message = request.args.get('message', '')
    return render_template('Home.html', message=message, patients=data['patients'])
        

