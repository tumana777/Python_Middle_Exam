# Validate firstname and lastname
def validate_name(name):
    # This try except block tries to get first name and last name
    try:
        fname, lname = name.split()
    except:
        # If there is a any error to get first name and last name, returns false
        print("Please, input valid info!")
        return False
    # If get first name and last name, check if not numbers in it
    if not fname.isalpha() or not lname.isalpha():
        print("Please, input valid info!")
        return False
    # If everything is validated, function returns true
    return True

# Validate unique number
def validate_number(student_list, number):
    
    if not number.isdigit():
            print("Please, input valid number!")
            return False
    for student in student_list:
                if student.roll_number == number:
                    print("Roll number is already in list!")
                    return False
    return True

# Validate student grade
def validate_grade(grade):
    grades = ["A", "B", "C", "D", "E", "F"]
    if not grade in grades:
        print("Please, input valid grade!")
        return False
    return True

# Validate Student Info
def validate_student(student_list):
    counter = 0
    while counter < 3:
        name = input("Please, input student name: ").strip().title()
        if not validate_name(name):
            counter += 1
            continue
        counter = 0
        break
    while counter < 3:
        number = input("Please, input student roll number: ")
        if not validate_number(student_list, number):
            counter += 1
            continue
        counter = 0
        break
    while True:
        grade = input("Please, input student grade: ").upper()
        if not validate_grade(grade):
            counter += 1
            if counter == 3:
                return
            continue
        break
        
    return name, number, grade

# Create Student Class
class Student:
    # Initialize parameters
    def __init__(self, name, roll_number, grade):
        self.id = 0
        self.name = name
        self.roll_number = roll_number
        self.grade = grade
        
    # Magic method to return student class info instead displaying just object
    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Roll Number: {self.roll_number}, Grade: {self.grade}"

# Create StudentManager Class
class StudentManager:
    # At the beginning, student list is empty
    student_list = []
    
    # This method adds student object in students list
    def append(self):
        try:
            name, roll_number, grade = validate_student(self.student_list)
        except:
            print("Exit...")
        else:
            new_student = Student(name, roll_number, grade)
            new_student.id = len(self.student_list) + 1
            self.student_list.append(new_student)

        
    def display_students(self):
        for student in self.student_list:
            print(student)
        
# Create univercity example by StudentManager class
university = StudentManager()