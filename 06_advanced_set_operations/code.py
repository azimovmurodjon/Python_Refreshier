friends = {"Bob", "Tony", "Chris"}
abroad = {"Bob", "Chris"}

#This method will colculate wil identify
local_Friends = friends.difference(abroad)
print(local_Friends)

#This method will return empty set()
local_Friends = abroad.difference(friends)
print(local_Friends)