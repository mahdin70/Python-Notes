# In Python, we don't actually assign values to the variables.
# Instead, Python gives the reference of the object(value) to the variable.

# When we write num1 = 10 , Python understands it's an integer
# Again, when we write num2 = 10.6 , Python understands it's a float 

# Python is a type-inferred language, [ automatic detection of the type of an expression in a formal language]
# So you don't have to explicitly define the variable type. 

num1 = 5
num2 = 10

sum = num1+num2  #here sum variable stores the addition result , so it's also an integer
print(sum)

#Assigning new values to the variables 
num1 = 15
num2 = 28  
sum = num1+num2   #sum variable containing the modified result
print(sum)

Hisname = "John"     #Here the value "John" referencing that this variable holding string 

# String variables can be within the " " or ' ' quotation 

print(Hisname +" is a Software Engineer at Google")

Hisname = "Jacky"    #new value assigning to Hisname or you can use extra variable

print("His younger brother "+ Hisname + " is an army officer")



# If you want to set a specific Data Type for a variable , that can be done with casting 

x = int(3);
y = str("Mukit")
z = bool(True)

# To get the data type in Python :

print(type(x))
print(type(y))
print(type(z))

###################################################################################################

"""

# Python Data Types


#   Example	                                    Data Type	
#   x = "Hello World"	                         str	
#   x = 20	                                     int	
#   x = 20.5	                                 float	
#   x = ["apple", "banana", "cherry"]	         list	
#   x = ("apple", "banana", "cherry")	         tuple	
#   x = range(6)	                             range	
#   x = {"apple", "banana", "cherry"}	         set	
#   x = frozenset({"apple", "banana", "cherry"}) frozenset	
#   x = True	                                 bool	
#   x = b"Hello"	                             bytes	
#   x = bytearray(5)	                         bytearray	
#   x = memoryview(bytes(5))	                 memoryview

"""

# Python Allows to assign multiple values in a single line 

x,y,z = 5,10,15

print(x+y)  # -> 15
print(y+z)  # -> 25
print(z+x)  # -> 20

m,n,o = "Mukit" , "Mahmud" , "Hasib"

print(m)
print(n)
print(o)


# One value to multiple variables 

x=y=z="Pera nai chill" 
print(x+" "+y+" "+z)


#If you have a collection of values in a list, tuple etc. Python allows you to extract the values into 
# variables.This is called unpacking.

fruits = ["Apple", "Banana", "Cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)



# Global Variable : Variable that is declared outside of the function and applicable for all the 
# following function 
# To declare a local variable [ inside the function ] as global variable , you have to use the keyword
# "global"