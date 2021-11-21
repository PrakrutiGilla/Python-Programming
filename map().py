#The map() function applies a given function to each item of an iterable (list, tuple etc.) 
#and returns a list of the results.

def cube(x):
    return x**3
n=list(map(cube,range(1,6))) #passing single iterator
print(n)

#or
n=list(map(lambda x:x**3, range(1,6)))
print(n)   

def add(x,y): 
    return x+y
n1=range(1,5)
n2=range(1,5)
n=list(map(add,n1,n2)) #passing multiple itearators
print(n)

#or 
n=list(map(lambda x,y:x+y ,n1,n2))
print(n)

def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))

print(x)
