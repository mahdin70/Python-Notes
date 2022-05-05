# Arithmetic Operators 

"""
+	Addition	
-	Subtraction	
*	Multiplication
/	Division
%	Modulus	
**	Exponentiation
//	Floor division

"""

x = 20
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)     # Will work as pow(x,y) -> 20 ^ 4
print(x // 2.3)   # Will print the floor value of the division which is 8 [ Original value 8.69 ]

#--------------------------------------------------------------------------------------------------------

# Identifying Operator :

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

#---------------------------------------------------------------------------------------------------------

# Bitwise Operator :

#  Let x = 10 (0000 1010) and y = 4 (0000 0100)

#   &	 Bitwise AND	      x & y = 0 (0000 0000)
#   |	 Bitwise OR	          x | y = 14 (0000 1110)
#   ~	 Bitwise NOT	       ~x = -11 (1111 0101)
#   ^	 Bitwise XOR	      x ^ y = 14 (0000 1110)
#   >>	 Bitwise right shift  x >> 2 = 2 (0000 0010)
#   << 	 Bitwise left shift	  x << 2 = 40 (0010 1000)

#--------------------------------------------------------------------------------------------------------

# Comparison Operator :

# ==	Equal	                    x == y	
# !=	Not equal	                x != y	
# >  	Greater than	            x > y	
# >=	Greater than or equal to	x >= y	
# <=	Less than or equal to       x <= y

#-------------------------------------------------------------------------------------------------------

# Membership Operator 

string1 = "Agent x is very good at shooting!"
if "Agent" in string1:                   # Checks if the substring "Agent" is the member of the string1
    print("This substring is present")

print("z" not in string1)    # Will Return True because z is already not present in the string1

