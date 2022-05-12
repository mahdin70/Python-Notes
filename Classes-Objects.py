
# Python is a Object Orineted Language. So it has all of the OOP fetures like Classes/Objects?Inheritance etc.
#****************************************************************************************************************
# Class : Class is like a blueprint for creating Objects ! 

from io import BufferedRandom
from mmap import ALLOCATIONGRANULARITY


class DemoClass:    # Creating Class
    Name = "John"
    Age = 5


Child1 = DemoClass()   # Creating instance of Child1 Object of DemoClass()

print(Child1.Name)
print(Child1.Age)

print("\n")
class Car:

    Brand = "Toyota"
    Model = "Alion"
    CC = 1500

Car_1 = Car()
print(Car_1.Brand)
print(Car_1.Model)
print(Car_1.CC)

print("\n")

#****************************************************************************************************************
# the __init__() function to assign values to object properties,
# or other operations that are necessary to do when the object is being created

class SportsCar:
    def __init__(Car,Brand,Model,CC):       # First parameter [Car] refers to the currect instance which is called Self parameter
        Car.Brand = Brand
        Car.Model = Model
        Car.CC = CC

Sport = SportsCar("Porsche","Tycan",4000)
print(Sport.Brand)
print(Sport.Model)
print(Sport.CC)


#****************************************************************************************************************
# if you create an empty or undefined class for some reason , use pass as the class body to avoid error 

class AjairaClass :
    pass

# Use Pass keyword when you donot define any class property or method 
#****************************************************************************************************************




