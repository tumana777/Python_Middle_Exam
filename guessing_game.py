'''
This is guessing game.
First asking user level difficulty and program will choise random number based user input.Then asks user to input guess
number, if user number not equals secret number, program hints user that number is lower or greater and also counts tries.
If user inputs not integers, program will give chance user to guess nimber again and prompts again, counter will increase
If user will guess secret number, prints number, amount tries and asks user if want to play again or not.
'''
# import random module
import random

# This function returns random number based given level
def difficulty(n):
    match n:
        case 1:
            return random.randint(1, 10)
        case 2:
            return random.randint(10, 100)
        case 3:
            return random.randint(100, 1000)
    return False

# This function returns text based given amount of tries
def print_result(counter):
    match counter:
        case 1:
            return "You're a mind reader!"
        case 2 | 3 :
            return "Most impressive."
        case 4 | 5 | 6:
            return "You can do better than that."
        case _:
            return "Better luck next time."

# This is main game function
def game(number):
    # First try counter is 1
    guess_counter = 1
    # Asking user to guess secret number
    guess = input("I have my number. Whats your guess? ")
    # This while loop tries to ask user input number, untill user will guess
    while True:
        # Checking if input value is digit or not
        if guess.isdigit():
            # This is hint for user
            if int(guess) < number:
                guess_counter += 1
                guess = input("Too low. Guess again: ")
            elif int(guess) > number:
                guess_counter += 1
                guess = input("Too high. Guess again: ")
            else:
                # If user will guess secret number, print number and amount of tries and break while loop
                print(f"Secret number is {guess}! You got it in {guess_counter} guesses!")
                print(print_result(guess_counter))
                break
        else:
            # If users inputs not integer, prompt again and counter will increase
            guess = input("Please, input only integers: ")
            guess_counter += 1

# This is app working loop
while True:
    try:
        # Try to get level form user
        level = int(input("Pick a difficulty level (1, 2 or 3): "))
        # If user inputs correct level, then will be generated secret number
        secret_number = difficulty(level)
        if secret_number:
            # If there is secret number, game function will work
            game(secret_number)
            # After game function ends, ask user wants to play agan or not
            play_again = input("Play again? y/n ").lower()
            if play_again != 'y' and play_again != 'yes':
                print("Goodbye!")
                break
    except:
        print("Please, input only integers!")
