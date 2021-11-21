#remove(), insert(), index() are used for this program


#Find the element in the list possessing the highest value. Split the element into two parts where
#first part contains the next highest value in the list and second part hold the required additive entity to get the highest value.
#Print the list where the highest value get splitted into those two parts.
#Sample input: 4 8 6 3 2
#Sample output: 4 6 2 6 3 2

n=list(map(int,input("enter numbers").split()))
m1=max(n)
i=n.index(m1)
print(i)
n.remove(m1)
m2=max(n)
n.insert(i,m2)
d=m1-m2
n.insert(i+1,d)
print(n)


#index() - used to find index of an element, takes index of first element as zero
eg: 
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
index = vowels.index('e')

#insert() - to insert an element at specified index
syntax: list.insert(position, element)

#3 functions can be used to remove element/elements from a list

1.remove() - it removes the specified element.

 eg: list = [1, 2, 3, 1]
     list.remove(2) # [1, 3, 1]

2.pop() -  removes an element at a given index, and will also return the removed item.

eg: numbers = [10, 20, 30, 40]
    ten = numbers.pop(0)
    print(ten) # 10

3.del -  to remove an element or slice from a list. ( used to remove sequence of elements). It is a keyword

eg:numbers = [50, 60, 70, 80]
   del numbers[1:2]
   print(numbers) # [50, 70, 80]
