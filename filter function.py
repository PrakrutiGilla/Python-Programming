#The filter() method filters the given sequence 
#with the help of a function that tests each element in the sequence to be true or not.
def evens(x):
    if(x%2==0):   # or return x%2==0 also works since == gives true or false as result
        return 1  #here returning 1/x/true gives same result
n=[1,2,3,4,5,6,7,8]    
evenslist=list(filter(evens,n))
print(evenslist)

def vowel(c):
    if(c=="a" or c=="e" or c=="i" or c=="o" or c=="u"):
        return 1
list1=list(filter(vowel,["a","p","j","i","o","s"]))
print(list1)

#or

def vowel(c):
    vowels=['a','e','i','o','u']
    if c in vowels:
        return 1
list1=list(filter(vowel,["a","p","j","i","o","s"]))
print(list1)
  
#using lambda function    
n=[1,2,3,4,5,6]    
oddlist=list(filter(lambda n:n%2!=0,n)    
print(oddlist)
