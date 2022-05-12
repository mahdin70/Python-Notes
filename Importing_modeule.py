import testmodule   # Exists is this Directory
import testmodule as tm  # Give a name after importing

testmodule.Hello("Mukit")

tm.Hello("Mahdin")

z = dir(testmodule)
print(z)

# dir() function prints all the existing methods in the imported module
# Output :
# ['Hello', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__'] 