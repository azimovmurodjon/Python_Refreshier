## This is While Look App
# number = 7
# while True:
#     user_input = input("would like to play? (Y/n) ")
#     if user_input == "n":
#         break
#     user_number = int(input("Guess our Number: "))
#     if user_number == number:
#         print("You guessed correcty!")
#     elif abs(number - user_number) == 1:
#         print("You were off by one")
#     else:
#         print("Sorry, it's wrong!")

#Working on ForLoop
friends = ["Rolf", "Jen", "Bob", "Anne"]

for friend in friends:
    print(f"{friend} is my friend.")

for friend in range(4):
    print(f"{friend} is my friend.")