

print(10 == 9)   # False
print(10 > 9)    # True
print(10 < 9)    # False

# There is a bool function which denotes if the given argument is true or false

x = 69
y = "Mahdin"

print(bool(x))    # True
print(bool(y))    # True 


# A function can also return Boolean value 

def randomfunction():
   return True

if randomfunction():   # Checking if the function return true or not 
 print("Yes,True!")
else:
 print("No,False!")