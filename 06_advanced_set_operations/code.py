friends = {"Bob", "Tony", "Chris"}
abroad = {"Bob", "Chris"}

#This method will colculate wil identify
local_Friends = friends.difference(abroad)
print(local_Friends)

#This method will return empty set()
local_Friends = abroad.difference(friends)
print(local_Friends)

#This method will United all friends together
local = {"Rolf"}
abroad = {"Bob", "Anne"}

friends = local.union(abroad)
print(friends)

#This method will print Duplicate one
art = {"Bob","Jen","Rolf","Charlie"}
scince = {"Bob","Jen","Adam","Anne"}

both  = art.intersection(scince)
print(both)


# Create a list, called my_list, with three numbers. The total of the numbers added together should be 100.
my_list = [20, 30, 50]
# Create a tuple, called my_tuple, with a single value in it
my_tuple = 15,
# Modify set2 so that set1.intersection(set2) returns {5, 77, 9, 12}
set1 = {14, 5, 9, 31, 12, 77, 67, 8}
set2 = {5, 77, 9, 12}
set1.intersection(set2)
