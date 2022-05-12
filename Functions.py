# You have to use "def" keyword to define a function :
def func():
    print("Hello, this is the function calling !")

func()     # -> Calling the function 


#****************************************************************************************************************
# Function with arguments :

def Hello(User):
    print("Hello,Mr."+User+". Welcome to Python!")

x = input("Enter User Name: ") 
Hello(x)


def Recieption(Name,Fruit):
    print("Hello,Mr."+ Name +". Here is "+ Fruit +" for you in the table.")

Recieption("Mukit","Orange")

#****************************************************************************************************************
# If number of parameters is not known, just add an asterisk(*) before parameter's name

def fruits(*name):    # By this we can give as many as we want as our parameter
    print("The most delicious fruits is "+ name[3])   # Accessing 4th item from our parameter's list which is a tuple

fruits("Apple","Banana","Orange","Lichi","Coconut","Mango")


#****************************************************************************************************************
# Default Parameter :
# Defalult Parameter means it will be executed if there is no parameter in function calling 

def Name(User = "John"):
    print(User +" is a Criminal")

Name("Kyle")
Name()     # Will take the default parameter "John", as no parameter is given ! 

#***************************************************************************************************************
# Passing a list of Arguments :

def Find_Criminal(Name):
    for x in Name:
        print(x)

Criminal = ["John","Kyle","Peter","Smith"]    # -> Creating a Argument List 
Find_Criminal(Criminal)

#***************************************************************************************************************
# Python also has return statement like other programming Languages :

def Add(x,y):
    return x+y    # -> The Return Statement 

Sum = Add(10,5)
print(Sum)

















































