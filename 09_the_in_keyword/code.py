friends = ["Bob", "Jen", "Tom"]
print("Jen" in friends)

#This method is giving true or false boolean result
movies_watched = {"The Matrix", "Green Bool", "Her"}
user_movie = input("Enter Somethins you've watched recently: ")

if user_movie in movies_watched:
    print(f"I've watched { user_movie} too!")
else:
    print("I haven't watched  that yet.")

#Majic Number App

number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == ("y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    else:
        print("Sorry, it's wrong!")

number = 15
user_input = input("Enter 'y' if you would like to play: ")

if user_input in ("y", "Y"):
    user_input = int(input("Guess our Number: "))
    if user_input == number:
        print("You guessed correcty!")
    else:
        print("Sorry, it's wrong!")