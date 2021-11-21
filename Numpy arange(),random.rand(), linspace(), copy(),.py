import numpy as np

"""arange()"""
a=np.arange(0,10) #similar to range() in lists
print(a)
#o/p : [0 1 2 3 4 5 6 7 8 9]

a=np.arange(0,10,2) #step=2
print(a)
#o/p: [0 2 4 6 8]

a=np.arange(0,9).reshape(3,3)
print(a)
#o/p: [[0 1 2]
#      [3 4 5]
#      [6 7 8]]

"""
linspace() - gives mentioned no of points between 2 values
linspace(start,stop,no.of points)
It gives equally divided points"""

print(np.linspace(0,6,10))
#O/P:[ 0.         0.66666667 1.33333333 2.         2.66666667 3.33333333
#      4.         4.66666667 5.33333333 6.        ]

print(np.linspace(12.5,20,5))
#O/P: [12.5   14.375 16.25  18.125 20.   ]


""" copy() - copies values from one array to another while keeping their memory spaces different """
""" syntax: a=b.copy() , values in b are copied to a"""

""" ones() - prints all ones"""

print(np.ones(4,dtype=int)) 
print(np.ones((2,3),dtype=float))

""" random.rand() - prints random values from 0 to 1 in the given shape """
""" random.randint(start,end,no of values) - prints random numbers between give start and end values """

print(np.random.rand(2,3))
#o/p:[[0.58380756 0.60172976 0.79722225]
#    [0.58437397 0.70588808 0.75823072]]


print(np.random.randint(0,100,8))
#o/p: [78 83 81 10 20 19 93]

print(np.random.randint(0,100,7).reshape(2,4))

print(np.random.randint(100,size=(3,3))
#o/p: [[56,89,78],
#      [90,97,45],
#      [63,76,34]]
