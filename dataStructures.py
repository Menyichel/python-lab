#lists - ordered and changeable
list1 = ["apple", "banana", "cherry"]
print(list1)
for x in list1: # for loop to access all
  print(x)
list1.append("orange") # append item to the list
list1.insert(1, "orange") # to insert an item at specified index
list1.remove("banana") # remove an item
list1.pop()
del list1[0] # removes the specified index
list1.clear() # empities the list
mylist = list1.copy() # copies the list
mylist1 = list(list1) # another way to copy

# joining lists
list11 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list3 = list11 + list2
print(list3)
# another way to join
list11 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list11.append(x)

print(list11)

# Use the extend() method to add list2 at the end of list1:
list11 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list11.extend(list2)
print(list11)


#A tuple is a collection which is ordered and unchangeable.
tuple1 = ("apple", "banana", "cherry")
print(tuple1)
print(tuple1[2:5])
print(tuple1[-4:-1])

#conversion bitween lists and tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print(x)

#loop in tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

#items cannot remove from the tuple but deleting tuple is possible
tuple3 = ("apple", "banana", "cherry")
del tuple3



# A set is a collection which is unordered and unindexed. 
# In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}
print(thisset)
for x in thisset:
  print(x)
thisset = {"apple", "banana", "cherry"}

thisset.add("orange")# adding one item
thisset.update(["orange", "mango", "grapes"]) # adding multiple items
thisset.remove("banana") # removing an item if item doesnot found error
thisset.discard("banana") # removing an item if no item no error
print(thisset)
x = thisset.pop()
thisset.clear() # empties the set
del thisset # deletes the set completly

# Join Two Sets
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set3 = set1.union(set2)
print(set3)

set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}

set1.update(set2) # The update() method inserts the items in set2 into set1:
print(set1)



# DictionaryA dictionary is a collection which is unordered, changeable and indexed.

mydict = {
  "Name": "Menyichel",
  "FName": "Beiza",
}
print(mydict)

# Accessing Items
x = mydict["Name"]
Y = mydict.get("Name")
# Change Values
mydict["Name"] = "Dawit"

for x in mydict: # LOOP
  print(x)

# use the values() function to return values of a dictionary:
for x in mydict.values():
  print(x)

# Loop through both keys and values, by using the items() function:
for x, y in mydict.items():
  print(x, y)

# Adding Items
mydict["color"] = "red"
print(mydict)
del mydict["FName"]
mydict.clear() #The clear() keyword empties the dictionary:

del mydict
