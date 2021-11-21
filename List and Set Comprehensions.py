#Comprehensions in Python provide us with a short and concise way to construct new sequences (such as lists, set, dictionary etc.) 

List Comprehension
"""syntax: [expression for item in iterable] (only for)
        [expression for item in iterable if conditional] (for, if)
        [exp if conditional else statement for item in iterable] (for, if-else) """

print([[i,j] for i in range(0,2) for j in range(0,2)])
#o/p: [[0, 0], [0, 1], [1, 0], [1, 1]]

x=2,y=2,z=2,n=3
print( [[i,j,k] for i in range(x) for j in range(y) for k in range(z) if(i+j!=3)])
#o/p: [[0, 0, 0], [0, 0, 1], [0, 0, 2], [0, 1, 0], [0, 1, 1], [0, 1, 2], [1, 0, 0], [1, 0, 1], [1, 0, 2], [1, 1, 0], [1, 1, 1], [1, 1, 2]]

print([x for x in range(0,6)])
#o/p: [0, 1, 2, 3, 4, 5]

print([i for i in "human"])
#o/p: ['h', 'u', 'm', 'a', 'n']

print([i for i in range(0,100,10)])
#o/p: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

print([i*i for i in range(0,10)])
#o/p: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print([x for x in range(100) if x % 3 == 0 if x % 5 == 0]) (nested if stmts)
#o/p: [0, 15, 30, 45, 60, 75, 90]

Set Comprehensions

input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7] 
  
set_using_comp = {var for var in input_list if var % 2 == 0} #In set comprehensions we have "{}" instead of"[]"
  
print("Output Set using set comprehensions:", 
                              set_using_comp)

#output: Output Set using set comprehensions: {2,4,6}
