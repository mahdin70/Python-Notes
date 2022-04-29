# Python Allows Three Types of Numbers :
# int , float , complex 

x = 5        #int
y = 10.38    #float
z = 5+3j     #complex

print(type(x))
print(type(y))
print(type(z))

print(z.real)  # Prints the real part of z 
print(z.imag)  # Prints the imaginary part of z 


# Converting to another type from one type 

x = 10
y = 5.86
z = 7+10j

# Type-Casting                  -> It is not possible to convert complex type to another types

a = float(x)
b = complex(y)
c = int(y)

print(type(a))
print(type(b))
print(type(c))


# Python has a "random" module to work with random numbers 

import random

print(random.randrange(1,25))    # Printing random number every time between 1 and 25  


# Python has the feature of Type-Casting 

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3


x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


x = str("s1") # x will be 's1'
y = str(2)    # y will be '2'
z = str(3.0)  # z will be '3.0'

