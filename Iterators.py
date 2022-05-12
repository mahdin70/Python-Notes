
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get 
# an iterator from.All these objects have a iter() method which is used to get an iterator

lists = ["Mukit","Mahmud","Hasib","Abu","Maruf"]
iterators = iter(lists)

print(next(iterators)) # -> Mukit
print(next(iterators)) # -> Mahmud
print(next(iterators)) # -> Hasib

#****************************************************************************************************************
# Iterating through a String :

string = "Floccinauchinihilipilification"
itre = iter(string)

print(next(itre)) 
print(next(itre))
print(next(itre))
print(next(itre))
print(next(itre))
print(next(itre))



















