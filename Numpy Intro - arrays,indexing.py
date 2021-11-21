""" Numpy is fast and is used very frequently.
Numpy has c bindings to it. So,it performs operations quickly. This is one of the reasons why it is used extensively in
machine learning algorithms."""
       

import numpy as np
l=[1,2,3,4]
a=np.array(l)#converts list to array using array()
print(a)#prints array
print(a.shape)#shape - gives no of rows and coloumns of the array

# 2D ARRAY  ( 2D array has 2 opening and closing brackets , in 3D array there will be 3 brackets)
l1=[1,2,3,4]
l2=[5,6,7,8]
l3=[9,10,11,12]
ar=np.array([l1,l2,l3])#creates 2D array using 3 lists 
print(ar)
print(ar.shape)
print(ar.reshape(6,2))#reshape(rows,coloumns) reshapes the array by changes no of rows and coloumns and prints the array.
                      #But it does not alter original array.

#INDEXING
#arrayname[ : , : ] leftside indicates rows and rightside indicates coloumns

print(ar[0:2,0:2])
print(ar[0:2,2:])
print(ar[1:3,2:])
print(ar[1:3, : ])#prints last 2 rows
print(ar[ : , : ])#prints all elements
