
# Python strings are surrounded by either " " (double quotes) or ' ' (single quotes)

a = "Hehe Boi"
print(a)        # Prints the string 
print(len(a))   # This counts the length of the string with the white space 

char_number = len(a) - a.count(" ")   # a.count(" ") counts the spaces in that string
print(char_number)      # char_number holds the character number after subtracting the spaces 


# Multiline String :

x = """ Roses are Red,
 Violates are blue,
 I Love you """

print(x)


# Strings are basically arrays in Python like other languages 

a = "Pera nai Chill"
print(a[0])     # Will print "P" 



# To check if a certain phrase or character is present in a string, we can use the keyword "in"

pera = "Ami to vala na vala niyai thaiko"

print("vala" in pera)        # This will print "True"  because "vala" exist in that string - pera 

if "Ami" in pera:            # Using If to check the presence of that sub-string
 print("Yes, Ami exists")



# To check if a certain phrase or character is NOT present in a string, we can use the keyword -> not in

mystr = "Valo achi valo theko , Akash er thikanay chithi likho"
print("nodi" not in mystr)   # Will Print "True" because "nodi" doesn't exist in the -> mystr 

if "nodi" not in mystr:
 print("No, it doesn't exist")



# Slicing :
# You can return a range of characters by using the slice syntax.
# Specify the start index and the end index, separated by a colon, to return a part of the string.

text = "Eid Mubarak everyone"
print(text[2:10])  # This will print the string index starting from 2 and ends at 10th position

# Eid Mubarak everyone
# 012345678910

# If you want to slice from the start to a certain position : the syntax is 

print(text[:12])   # Will print till 12th Character from the starting position

print(text[5:])    # Will print till the end from the 5th position 