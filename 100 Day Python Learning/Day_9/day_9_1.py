programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again."}

# Retriving Item from Dictionary
# print(programming_dictionary["Bug"])

# Adding New Item to Dictionary
programming_dictionary["Loop"] = "The Action of doing something over and over again"

# print(programming_dictionary)

# Create an Empty Dictionary
empty_dictionary = {}

# Wipe an Existiong dictionary
# programming_dictionary = {}
# print(programming_dictionary)

#Edit an item in a Dictionary
# programming_dictionary["Bug"] = "A Month In your Computer"
# print(programming_dictionary)

#Loop Through a Dictionary it will return only Key
for key in programming_dictionary:
    print(key)
  #if you want to get a key and Value just print Proggramming_dictionary by adding [key] as well
    print(programming_dictionary[key])
