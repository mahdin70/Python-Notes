
# Lists are used to store multiple things in a single variable 
# They are ordered, changable and can be duplicated 

list = ['apple','bananna','orange']  # Elements is list are like array, you can access them like array

print(list[0])    # -> Will Print apple 

print(list) # -> Will print the list as it is  

print(len(list)) # -> This len() function  will print the total item number of the list 

#*********************************************************************************************************************

# List items can be any of the Python Data types [ int , float ,  bool , string ]

intList = [1,2,5,8,6]
boolList = [True,False,False,True]
stringList = [ "Dhaka","New York","London","Manchester"]
 
print(type(intList))        # Printing the data types of the list 
print(type(boolList))
print(type(stringList))

# A list can contain various data types also :

list = [ 1 , True , "Cat",5.86]

#**********************************************************************************************************************

# Difference between collections of data types 

# List is a collection which is ordered and changeable. Allows duplicate members.
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
# Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
# Dictionary is a collection which is ordered** and changeable. No duplicate members.

#**********************************************************************************************************************

# Adding items to a list -> using append() method

mylist = [ "Cow","Cat","Dog","Hare"]

mylist.append("Sheep")      # Will Append to the existing list as the last item 

print(mylist)

#*********************************************************************************************************************

# Adding items to a list with specific index -> using insert() method 

mylist = [ "Cow","Cat","Dog","Hare"]

mylist.insert(0,"Sheep")    # Inseting "Sheep" on the 0th index 

print(mylist)  # -> will print the list with sheep at 0th index !

#*********************************************************************************************************************

# Navigating the list :

# You can traverse through the list as the arrays using their position index like list[0] , list[1]  etc.
# You can access the last item of the list using the index -1 -> list [-1]

print(mylist[-1])   # -> This will print the last item of the list "Hare"

#*********************************************************************************************************************

# Two lists can be combined as a single list using the extend() method ! 

mylist1 = [ "Cow","Cat","Dog","Hare"]
mylist2 = [ "John","Peter","Amber","Johny"]

mylist1.extend(mylist2)

print(mylist1)  # -> Will print the extended list combining mylist1 and mylist2

#*********************************************************************************************************************

# Removing Specific item from the list using remove(item) method 

mylist1 = [ "Cow","Cat","Dog","Hare"]
mylist1.remove("Dog")
print(mylist1)    # -> Will print ['Cow', 'Cat', 'Hare']

# Removing Specific index using pop() method 

mylist2 = [ "John","Peter","Amber","Johny"]
mylist2.pop(1)    # if you don't specify the index the pop() method will remove the last item from the list 
print(mylist2)    # -> Will print ['John', 'Amber', 'Johny']

# Removing Specific index using del command

mylist2 = [ "John","Peter","Amber","Johny"]
del mylist2[2]
print(mylist2)    # Will print ['John', 'Peter', 'Johny']

#*********************************************************************************************************************

#clear() method can empty the list , the list will exist after but no content will be there
mylist1 = [ "Cow","Cat","Dog","Hare"]
mylist1.clear()

#*********************************************************************************************************************

# Looping through a list 

mylist1 = [ "Cow","Cat","Dog","Hare"]
for x in mylist1:
    print(x) # -> Will print each item of the list seperately 

# Looping using range()

mylist2 = [ "John","Peter","Amber","Johny"]
for x in range(len(mylist2)):
    print(mylist2[x])


#*********************************************************************************************************************

# List comprehension 

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]   # -> The newlist[] will take the items from fruits[] which have "a" in them

print(newlist)  # -> Will print ['apple', 'banana', 'mango']

#*********************************************************************************************************************

# Sorting the list

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# Sorting in Descending Order 

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#*********************************************************************************************************************
# List methods 

#  append()	  Adds an element at the end of the list
#  clear()	  Removes all the elements from the list
#  copy()	  Returns a copy of the list
#  count()	  Returns the number of elements with the specified value
#  extend()	  Add the elements of a list (or any iterable), to the end of the current list
#  index()	  Returns the index of the first element with the specified value
#  insert()	  Adds an element at the specified position
#  pop()	  Removes the element at the specified position
#  remove()	  Removes the item with the specified value
#  reverse()  Reverses the order of the list
#  sort()	  Sorts the list


 





