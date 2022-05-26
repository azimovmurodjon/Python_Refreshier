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