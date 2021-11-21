#Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another list but in reverse order.
n=list(map(int,input("enter numbers").split()))
i=len(n)-1
print(i)
s=[]
while(i>=0):
    s.append(n[i])
    i=i-1
print(s)

#using reverse function will reverse the original list
s=[1,2,3,4]
s.reverse()
print(s)

#accessing elements in sub-lists
a=[[1,2,3],[4,5,6]]
i = 0
print(a[0])#prints [1,2,3]
print(a[0][2])# first value(0) indicates the sub list and second value indicates the element in the sub-list
while i<len(a):
  j = 0
  while j < len(a[i]):
    print (a[i][j])
    j = j+1
  i = i+1
    
