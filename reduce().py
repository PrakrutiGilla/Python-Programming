#It takes 2 elements from a single list in the beginning. 
#The result of the 2 elements is added to the next element (3rd) of the list and so on. The final result is stored at the end
"""
The reduce(fun,seq) function is used to apply a particular function 
passed in its argument to all of the list elements mentioned in the sequence passed along

Working:
1.At first step, first two elements of sequence are picked and the result is obtained.
2.Next step is to apply the same function to the previously attained result and the number just succeeding the second element and the result is again stored.
3.This process continues till no more elements are left in the container.
"""

from functools import reduce
lis = [ 1 , 3, 5, 6, 2, ] 
   
print ("The sum of the list elements is : ",end="") 
print (reduce(lambda a,b : a+b,lis))
l=reduce(lambda a,b : a+b,lis) #l=17 (the final result)
print(l)

