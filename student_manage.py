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
    # Checking if number is integer
    if not number.isdigit():
        # If number is not integer return false
            print("Please, input valid number!")
            return False
    # Checking if student number is already in list or not
    for student in student_list:
                if student.roll_number == number:
                    # If student number is already in list, returns false
                    print("Roll number is already in list!")
                    return False
    # If everything is validated, function returns true
    return True

# Validate student grade
def validate_grade(grade):
    # Create possible grades list
    grades = ["A", "B", "C", "D", "E", "F"]
    if not grade in grades:
        # Checking if inputted grade is not in list, return false
        print("Please, input valid grade!")
        return False
    # If everything is validated, function returns true
    return True

# Validate Student Info
def validate_student(student_list):
    counter = 0
    # This while loop gives user 3 tries to input valid name
    while counter < 3:
        name = input("Please, input student name: ").strip().title()
        # Calling this function checks name validation
        if not validate_name(name):
            # If name not valid, counter increases and prompts user again to input valid name
            counter += 1
            continue
        # If name is valid, counter will reset, breaks this while loop and begins next while loop
        counter = 0
        break
    # This while loop gives user 3 tries to input valid roll number
    while counter < 3:
        number = input("Please, input student roll number: ")
        # Calling this function checks roll number validation
        if not validate_number(student_list, number):
            # If roll number not valid, counter increases and prompts user again to input valid number
            counter += 1
            continue
        # If roll number is valid, counter will reset, breaks this while loop and begins next while loop
        counter = 0
        break
    # This while loop gives user 3 tries to input valid grade
    while True:
        grade = input("Please, input student grade: ").upper()
        # Calling this function checks grade validation
        if not validate_grade(grade):
            # If grade not valid, counter increases and prompts user again to input valid grade
            counter += 1
            # If user inputs not valid grade 3 times, this function will stop
            if counter == 3:
                return
            continue
        # If grade is valid, breaks this while loop
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