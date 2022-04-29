
# Working with Upper/Lower case  :
a = "Hello, my dear !"

print(a.upper())     # Converts to Upper case character 
print(a.lower())     # Converts to Lower case character

#-------------------------------------------------------------------------------------------------------

# Remove Whitespace Characters ->strip() :

x = "    Hello World    "
print(x.strip())  # Remove extra spaces in the beginning and the ending of the string 

#-------------------------------------------------------------------------------------------------------

# Replacing Character or Sub-String :

x = "Humpty dumpty sitting on a wall"
z = x.replace("dumpty","mumpty")    # Replacing dumpty with "mumpty"
print(z)

p = x.replace('w','b')  # Replacing the character 'w' with 'b'
print(p)

#-------------------------------------------------------------------------------------------------------

# Spliting String :
# The split() method returns a list where the text between the specified separator becomes the list items.
# You have define which character is spliting the whole string 

text = "I have apple, banana, pineapple, orange, lichi, papaya, watermelon"
print(text.split(','))   # Will return a list of each "comma(,)" separated sub-string

# Output : ['I have apple', ' banana', ' pineapple', ' orange', ' lichi', ' papaya', ' watermelon']

text = "The dog a cow a horse a bird"
print(text.split("a"))

# Output : ['The dog ', ' cow ', ' horse ', ' bird'] 

#------------------------------------------------------------------------------------------------------

# Formatting String : 
# The format() method takes all the arguments and place it to the respective placeholder defined by {}

string = "Roses are {} , Violates are {} , I {} you"
print(string.format("red","blue","love"))  

# The arguments will take the places of {curly braces} sequentially

#------------------------------------------------------------------------------------------------------

# Escape Characters : 
"""
\'	Single Quote	
\\	Backslash	
\n	New Line	
\r	Carriage Return	
\t	Tab	
\b	Backspace
"""
txt = "There is a \"Don\" among us"
print(txt)  # There is a "Don" among us 

#-----------------------------------------------------------------------------------------------------

# Various String Functions :

text = "A quick brown fox jumps over the lazy dog"

print(text.casefold())      # Converts to lower case
print(text.encode())        # Returns the encoded version of the string 
print(text.find("quick"))   # Returns 2 because "quick" starts from the index position 2
print(text.index("b"))      # Returns the index position of 'b'
print(text.isalnum())       # Returns True if all the characters in the string are alphanumeric / False
print(text.title())         # Converts the first characters of each words to Captial form 
print(text.swapcase())      # Converts upper to lowercase and lower to uppercase
