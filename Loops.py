# Python has two built in loops for and while 
# while loop is executed as long as 
print("First Loop")
i = 0
while i<7:
    print(i)
    i+=1

print("Second Loop")
j = 1
while j < 10:
    print(j)
    if j==9:
     break
    j+=2

print("Third Loop")
m = 2
while m < 20:
    print(m)
    if m==17:
     break
    m+=1




#*****************************************************************************************************************

# For loop is used for iterating over some sequences : it can be any of the collection of data types 
# [ List, tuple , Set , Dict ]
print("For Loop --------- :")
# Looping through a Tuple 
tuples=("Mango","Banana","Coconut")
for x in tuples:
    print(x)
print("\n")

# -> Output :
# Mango
# Banana
# Coconut
print("Second Loop :")
tuples=("Mango","Banana","Coconut","Berry","Apple")
for x in tuples:
    print(x)
    if x=="Berry":
        break

#*****************************************************************************************************************
print("Third Loop:")
for x in range(10):
    print(x)


# range(10) is not the values of 0 to 10, but the values 0 to 9
print("Fourth Loop:")
for x in range(0,50,5):    # -> 0 to 50 , difference 5
    print(x)



