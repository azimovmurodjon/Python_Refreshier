name = "Bob"

print(f"Hello, {name}")

name = "Rolf"

print(f"Hello, {name}")

name = "Bob"
greeting = "Hello, {}"
with_name = greeting.format(name)
with_name_two = greeting.format("Rolf")

print(with_name)
print(with_name_two)

longer_Phrase = "Hello, {}. Today is {}"
formatted = longer_Phrase.format("Rolf", "Monday")
print(formatted)
