# List of avaliable operators
operators = ["+", "-", "*", "/"]

# Create calculator class
class Calculator:
    # Initialize parameters
    def __init__(self, FirstNumber, SecondNumber):
        self.FirstNumber = FirstNumber
        self.SecondNumber = SecondNumber

    # Method for operations
    def operation(self):
        while True:
            # try to get operator from user
            try:
                operator = input("Please enter the operator: ")
                # Checking operator if avaliable
                if operator in operators:
                    return eval(f"{self.FirstNumber} {operator} {self.SecondNumber}")
                else:
                    print("Please, input correct operator!")
            # Catch error caused devide by zero
            except ZeroDivisionError:
                return "Impossible to devide by zero!"
            
# This function returns numbers
def numbers():
    while True:
        # Trying to get number 1 from user
        try:
            num1 = input("Please, input number 1: ")
            num1 = float(num1)
            break
        # Catch error
        except:
            print("Input only integers or floats!")
        
    while True:
        # Trying to get number 2 from user
        try:
            num2 = input("Please, input number 2: ")
            num2 = float(num2)
            break
        # Catch error
        except:
            print("Input only integers or floats!")
    # If numbers are valid, return yhis numbers
    return num1, num2

# Launch calculator
while True:
    print(f"List of available operators:\n{operators}")
    # Get numbers from function
    x, y = numbers()
    # Create Calculator object
    calculations = Calculator(x, y)
    result = calculations.operation()
    print(result)
    action = input("Do you want to calculate again? y/n ")
    # Finish while loop
    if action != "y":
        break