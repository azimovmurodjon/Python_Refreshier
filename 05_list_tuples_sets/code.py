#list you can put diffrent calliues as they have come between This Definses List
list = ["Bob", "Rob", "Todd"]
#Tuples you cant modifier, you can't add or remove varieble on tuple
tuple = ("Bob", "Rob", "Todd")
#Sets you can't have Duplicates, but you can add or remove eliments
sets = {"Bob", "Rob", "Todd"}

list[0] = "Smith"
print(list)

#this tuple functionality will fail Tuple can not be modifired
# tuple[0] = "Smith"
# print(tuple)

#you can not do it on set set is not alloud  for subscript notation
# sets[0] = "Smith"
# print(sets)

#You can append to List
list.append("Tom")
print(list)

list.remove("Rob")
print(list)

#Set will ignore Duplicates
sets.add("Anne")
sets.add("Bob")
print(sets)