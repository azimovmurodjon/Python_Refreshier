
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == ("y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    elif abs(number - user_input) == 1:
        print("You were off by one")
    else:
        print("Sorry, it's wrong!")