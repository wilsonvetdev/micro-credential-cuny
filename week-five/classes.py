# Python 3.9.1

# Wilson Ng - Week Five Day Three- 02/05/2021

class Vehicle:

    def __init__(self, type = "Unknown"):
        self.type = type 
    
    def display(self):
        print(f"type={self.type}")

first_car = Vehicle()
second_car = Vehicle("Car")
first_car.display()
second_car.display()

class Car(Vehicle):

    def __init__(self, type = "Car", name = "Unknown"):
        super().__init__(type = type)
        self.name = name
    
    def display(self, horsepower = None):
        if horsepower:
            print(f"type={self.type} name={self.name} horsepower={horsepower.get_horsepower()}")
        else: 
            print(f"type={self.type} name={self.name}")

first_car = Car()
second_car = Car(name = "Audi")
first_car.display()
second_car.display()

class Engine():

    def __init__(self, horsepower = "0"):
        self.horsepower = horsepower
    
    def get_horsepower(self):
        return self.horsepower

new_car = Car("Car", "Audi")
new_car.display(Engine("450"))

class Student():

    def __init__(self, name, grades = []):
        self.name = name
        self.grades = grades
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Grades: {self.grades}")
    
    def add_grade(self, grade):
        self.grades.append(grade)
    
    def remove_grade(self, grade):
        if grade in self.grades:
            self.grades.remove(grade)
    
april_student = Student("April")
april_student.add_grade(90)
april_student.add_grade(97)
april_student.add_grade(85)
april_student.add_grade(85)
april_student.display()
april_student.remove_grade(97)
april_student.display()