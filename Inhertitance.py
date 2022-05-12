
# Inheritance Concept in Python is same as other OOP Lamguages 
# In a broad sense ,Inheritance means inherit all the properties and methods from another class [Parent Class]
# The Class which is inheriting will be called "Child Class"

#*****************************************************************************************************************
# Parent Class : 

class Car:
    def __init__(car,brand,model,cc):
        car.brand = brand
        car.model = model
        car.cc = cc

    def printdetails(car):
        print("This is the car from "+car.brand+". It's Model is "+car.model+". This car has "+car.cc+" CC Engine")


mycar = Car("Toyota","Allion","1500")
mycar.printdetails()



# Child Class :   -> Inheriting the Parent Class "Car" as well as its properties and methods 

class SportsCar(Car):
    pass

lambo = SportsCar("Lamborgini","Hurracan","6000")
lambo.printdetails()



























