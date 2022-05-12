
# Tuple is a collection which is ordered and unchangeable.
# Tuples are written with round brackets.

mytuple = ("Jada","Amber","Will","Johny")   # Syntax of a tuple
print(mytuple)

# Tuple items are unchangeable , ordered and can have duplicate values 

tuple2 = ("Jada","Amber","Will","Johny","Will","Jada")
print(tuple2)

#*******************************************************************************************************************
# Finding Tuple Length 

print(len(tuple2))  # -> Will print 6

#*******************************************************************************************************************
# Tuple with a single item

x = ("Mahdin")    # This won't act as tuple because there is no comma (,) after that item
print(x)

x = ("Mahdin",)   # This is a tuple with a single element 
print(x)

#*******************************************************************************************************************
# Accessing Tuple Elements : [ Like Arrays ]

mytuple = ("Jada","Amber","Will","Johny")
print(mytuple[2])  # -> Accessing 3rd Element [ index 2]

# Tuples also have negative indexing like lists 
print(mytuple[-1]) # Accessing the last item of the tuple 

#*******************************************************************************************************************
# Range of indexes :

#                0        1        2         3         4        5        6
thistuple = ("Shuvro", "Nibir", "Mamun", "Shoumik", "Ridun", "Wasif", "Kawsar")
print(thistuple[3:6]) 

# -> Will print ('Shoumik', 'Ridun', 'Wasif')
# The search will start at index 3 [ included ] and end at index 6 [ not included ]

print(thistuple[:5]) # Accesing from beginning to before 5th index 
# -> Will print ('Shuvro', 'Nibir', 'Mamun', 'Shoumik', 'Ridun') 

print(thistuple[3:]) # Accessing from 3rd index to last index 
# -> Will print ('Shoumik', 'Ridun', 'Wasif', 'Kawsar')

#*******************************************************************************************************************
# Check Availability :

thistuple = ("Shuvro", "Nibir", "Mamun", "Shoumik", "Ridun", "Wasif", "Kawsar")

if "Shuvro" in thistuple:
    print("Yes,Shuvro Exists!")

if "Muaz" not in thistuple:
    print("No,Muaz Doesn't Exist")

#*******************************************************************************************************************
# Changing tuple values :
# As I said earlier , tuples are unchangeable so we cannot change its elements 
# Rather we can convert a tuple into a list, change the value of the list and again convert to tuple 


tuples = ("Shuvro", "Nibir", "Mamun", "Shoumik", "Ridun", "Wasif", "Kawsar")
lists = list(tuples)
lists[3] = "Muaz"
lists = tuple(lists)

print(lists)


#*******************************************************************************************************************
# Unpacking a tuple :

tuples = ("Shuvro", "Nibir", "Mamun", "Shoumik", "Ridun", "Wasif", "Kawsar")
(fiftynine,two,tweleve,fortyfour,fifty,twentynine,eight) = tuples
print(fiftynine)
print(two)
print(tweleve)
print(fortyfour)
print(fifty)


#*******************************************************************************************************************
#*******************************************************************************************************************
#*******************************************************************************************************************



# Sets are usually like tuples and lists but with curly braces 

myset = {"Mukit","Mahmud","Abu","Hasib"}
print(myset)

myset.add("Rifat")
print(myset)



myset.update(tuples)   # -> Adding another iterable [tuple] to the set 
print(myset)













