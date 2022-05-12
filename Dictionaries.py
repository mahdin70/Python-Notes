
# Dictionaries are used to store data values in "key : value" pairs.
# Dictionary is a collection which is ordered*, changeable and do not allow duplicates.

mydict = {"Name":"John" , "Height":"Six Feet" , "Age":"35"} # -> Here Name,Height,Age are the keys and rest are values 
print(mydict)


print(mydict["Height"])  # -> Accessing a value by the key [Height]

print(len(mydict))       # -> length is 3

#******************************************************************************************************************
#Accessing Dictionary items :  get() method 

mydict = {"Name":"John" , "Height":"Six Feet" , "Age":"35"}

z = mydict.get("Name")   # -> Accessing value of the "Name" key from the dictionary 
print(z)


#******************************************************************************************************************
# List of the Keys :
print(mydict.keys())
# -> Output : dict_keys(['Name', 'Height', 'Age'])

# Values of the keys 
print(mydict.values())
# -> Output : dict_values(['John', 'Six Feet', '35'])

# Getting the Pairs together:
print(mydict.items())
# -> Output : dict_items([('Name', 'John'), ('Height', 'Six Feet'), ('Age', '35')])


#******************************************************************************************************************
# Changing Values of keys :

mydict = {"Name":"John" , "Height":"Six Feet" , "Age":"35"}
mydict["Age"] = "45"
print(mydict)

# update() method 

mydict.update({"Height":"Five Feet"})
print(mydict)


#******************************************************************************************************************
# Dictionary methods :

# clear()	     Removes all the elements from the dictionary
# fromkeys()	 Returns a dictionary with the specified keys and value
# get()	         Returns the value of the specified key
# items()	     Returns a list containing a tuple for each key value pair
# keys()	     Returns a list containing the dictionary's keys
# pop()	         Removes the element with the specified key
# popitem()	     Removes the last inserted key-value pair
# setdefault()	 Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
# update()	     Updates the dictionary with the specified key-value pairs
# values()	     Returns a list of all the values in the dictionary





























