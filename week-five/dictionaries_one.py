# Python 3.9.1

# Wilson Ng - Week Five Day Two- 02/03/2021

print("---Exercise One---")
print(" ")

car = {"brand": "Audi", "model": "RS7", "color": "cement grey"}
car["transmission"] = "automatic"

for value in car.values():
    print(value)

print(" ")
print("---Exercise Two---")
print(" ")

for key, value in car.items():
    print(f"{key}: {value}")

print(" ")

for key in car.keys():
    print(f"{key} {car[key]}")

print(" ")

for value in car.values():
    print(f"{value}")

print(" ")
print("---Exercise Three---")
print(" ")

car_list = [
    {"brand": "Audi", "model": "RS7"},
    {"brand": "Audi", "model": "RS5"},
    {"brand": "Audi", "model": "TT RS"},
    {"brand": "Audi", "model": "Q8"},
    {"brand": "Audi", "model": "R8"},
]

for car in car_list:
    print(car["model"])


print(" ")
print("---Exercise Four---")
print(" ")


doctor_list = [
    {"name": "Dr.Seuss", "patient": {"first_name": "John", "last_name": "Doe"}},
    {"name": "Dr.Einstein", "patient": {"first_name": "Jane", "last_name": "Doe"}}
]

for doctor in doctor_list:
    print(f"{doctor['name']}: {doctor['patient']['first_name']} {doctor['patient']['last_name']}")
    

print(" ")
print("---Exercise Five--")
print(" ")

doctor_list = [
    {"name": "Dr.Seuss", "patients": ["Jim", "Jane", "Joan"]},
    {'name': 'Dr.Kim', 'patients': ['Karl', 'Khan']},
    {'name': 'Dr.Ruben', 'patients': ['Racheal', 'Robert', 'Raymond']}
]

for doctor in doctor_list:
    print(f"{doctor}")

print(" ")

for doctor in doctor_list:
    print(f"{doctor['name']}")

print(" ")

patients = ""

for doctor in doctor_list:
    doctor_name = doctor["name"]
    for value in doctor["patients"]:
        patients += value + " "
    
    print(f"{doctor_name} -{patients}")
    patients = ""

print(" ")
print("---Exercise Six--")
print(" ")

student_list = [
    {"name": "John", "grades": [90, 84, 59]},
    {"name": "Sarah", "grades": [73, 80, 55]},
    {"name": "Lara", "grades": [95, 72, 83, 44]}
]

grades = ""
avg = 0
passing_grades = []

for student in student_list:
    student_name = student["name"]
    for grade in student["grades"]:
        if grade >= 60:
            grades += str(grade) + " "
            passing_grades.append(grade)

    print(student_name, grades, "- Avg = ", sum(passing_grades)/len(passing_grades))
    grades = ""
    passing_grades = []
