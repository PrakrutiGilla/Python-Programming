#Write a program to shift every element of a list to circularly right. E.g.-
INPUT : 1 2 3 4 5
OUTPUT : 5 1 2 3 4


n=list(map(int,input("enter numbers").split())) #if 5 elements are given
last=len(n)-1 #last = 4
n.insert(0,n[last])# one element inserted. now, len = 5. so we should delete 5th element. 
n.pop(len(n)-1)# since last holds 4. don't put last in pop. once again write len(n)-1 (5th element)
print(n)

#or

a = [1,2,3,4,5]
b = [a[len(a)-1]]+a[:len(a)-1] #add the slices
print(b)
a = b
print(a)

#prg to print unique elements in a list (consider each element only once)

l=[1,2,3,5,9,3,7,9]
n=[]
n.append(l[0])
for i in l:
    if i not in n:
        n.append(i)
print(n)       

