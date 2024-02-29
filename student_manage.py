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

# Checking if number is integer
def check_number(number):
    if not number.isdigit():
        # If number is not integer return false
            print("Please, input valid number!")
            return False
    return True

# Validate unique number
def validate_number(student_list, number):
    # Checking if number is integer
    if not check_number(number):
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
    while True:
        name = input("Please, input student name: ").strip().title()
        # Calling this function checks name validation
        if not validate_name(name):
            # If name not valid, counter increases and prompts user again to input valid name
            counter += 1
            if counter == 3:
                return
            continue
        # If name is valid, counter will reset, breaks this while loop and begins next while loop
        counter = 0
        break
    # This while loop gives user 3 tries to input valid roll number
    while True:
        number = input("Please, input student roll number: ")
        # Calling this function checks roll number validation
        if not validate_number(student_list, number):
            # If roll number not valid, counter increases and prompts user again to input valid number
            counter += 1
            if counter == 3:
                return
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

# This is linear search function
def linear_search(lst, n):
    
    for i in range(len(lst)):
        if lst[i].roll_number == n:
            return lst[i]
    return False

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
    
    # This method returns if library is empty or not
    def empty(self):
        return len(self.student_list) == 0
    
    # This method adds student object in students list
    def append(self):
        print("Adding Student...")
        # Try to get student inforamtion from outer function
        try:
            name, roll_number, grade = validate_student(self.student_list)
        except:
            # If student inforamtion can not get, print 
            print("Student can't be added.")
        else:
            # If input student inforamtion is valid, add student to university
            new_student = Student(name, roll_number, grade)
            new_student.id = len(self.student_list) + 1
            self.student_list.append(new_student)
            
    # Student search method
    def search(self):
        # Checking if student list is empty or not
        if self.empty():
            print("Student list is empty!")
        else:
            # Give user 3 tries to input valid number
            for _ in range(3):
                roll_number = input("Please, input roll number for search: ")
                # Checking input value
                if check_number(roll_number):
                    # If input value is valid, then begins searching and for cycle will stop
                    student = linear_search(self.student_list, roll_number)
                    if student:
                        print(f"Student you search, there is full info -> {student}")
                    else:
                        print("There is no student in the university with this roll number.")
                    return
            print("Searching ended.")


        
    def display_students(self):
        for student in self.student_list:
            print(student)
        
# Create univercity example by StudentManager class
university = StudentManager()