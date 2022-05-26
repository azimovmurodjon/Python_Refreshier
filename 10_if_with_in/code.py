 # Majic Number Ap
#Will be able to enter Upper and lowwer case for Y diffrent method
number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == ("y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    else:
        print("Sorry, it's wrong!")

#Will be able to enter Upper and lowwer case for Y diffrent method
number = 15
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    else:
        print("Sorry, it's wrong!")

#Will be able to enter Upper and lowwer case for Y diffrent method and gues was close or not will mentioned
number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == ("y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    elif abs(number - user_input) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")