
# lambda is a compact and small function in Python
# It can take any number of arguments but can only have one expression ! 

# Syntax  ->  lambda [arguments]:expression

d = lambda x,y,z : (x+y)/z
print(d(10,8,2))


# Lambda can be used inside other functuions 

def Dividebytwo(n):
    return lambda a:a/n

divide = Dividebytwo(2)
print(divide(20))
print(divide(35))
   