friends = ["kevin", "karen", "jim", "oscar", "toby"]
#lists can hold any type
#friends[0] first
#friends[-1] last
#friends[-2] second last

# print(friends[1:])# 1 onwards
# # [:3] 0 to 3
# # print(friends[1:3]) 1 to 3

lucky_numbers = [4, 8, 15, 16, 23, 42]

friends.extend(lucky_numbers) # adds lucky numbers onto friends

print(friends)


friends = ["kevin", "karen", "jim", "oscar", "toby"]
friends.append("creed") # adds it on to the end of the list
print(friends)

friends.insert(1, "jazz")
print(friends)

friends.remove("karen")
print(friends)

friends.clear() # gets rid of all elements in the list
print(friends)

friends = ["kevin", "karen", "jim", "oscar", "toby"]
friends.pop()
print(friends)

print(friends.index("karen")) # gives error when something is not in the list

friends.count("karen") # returns how many times karen is in the list

friends.sort() #sorts the list in ascending order
lucky_numbers.reverse() #reversed the order of the list

friends2 = friends.copy() #all same attributes of friends but not the same list







