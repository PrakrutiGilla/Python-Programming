#Write a program to check if elements of a list are same or not it read from front or back.
a=[1,2,3,4,5,4,3,2,1]
i=0
j=len(a)-1
f=0
while(i<len(a)):
  if(a[i]!=a[j]):
    f=1
    break
  i=i+1
  j=j-1

if(f==1):
  print("not same")
else:
  print("same")

#Make a list by taking 10 input from user. Now delete all repeated elements of the list.
a=[1,2,3,4,3,2]
b=[]
for i in a:
    if i not in b:
      b.append(i)
print(b)

#or
a=[1,2,3,4,3,2]
b=(list(set(a))#set has only unique elements
print(b)

#del() - function to delete elements  
