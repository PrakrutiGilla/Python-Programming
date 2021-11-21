#dictionary for single element
d={}
user=input("enter name")
pw=input("enter pw")
d[user]=pw
print(d)

#dictionary for multiple elements

user=list(map(str,input("enter name").split()))
pw=list(map(str,input("enter pw").split()))
d=dict(zip(user,pw)) #zip() - combines user and pw. dict()- converts zip into dictionary
print(d)
