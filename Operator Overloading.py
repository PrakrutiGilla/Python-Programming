#operation overloading means operations/functions defined by user for objects

# operators like +,-,*,/,%,>,<, etc only work for variables, do not work for objects.
#int, float, str have built in function for these operators like "+" b/w 2 integers indicates __add__()
#(reminder: these functions only work b/w varaiables of same type as each type has different built-in function for same operation(add,sub))
#but these functions are not defined for objects
#so we have to define these (__add__(), __mul__(), __lt__() etc) functions for objects, as done below
#we do this by taking object attributes and converting them into variables and then perform operations, like addition.


class student:

    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2

    def __add__(self,other): #addition #s1+s2

        m1=self.m1+other.m1  #s1 is object but self.m1 is integer
        m2=self.m2+other.m2
        s3=student(m1,m2) #this initializes m1 and m2 values to s3 by calling __init__ function.
        return s3
   """ s1 - self, s2 - other. m1 and m2 are variables
       addition is performed b/w 2 values and stored in m1 and m2.
       result should also be in type of class. so both m1 and m2 are assigned to s3 declared as class student"""

    def __sub__(self,other): #subtraction
        m1=self.m1-other.m1
        m2=self.m2-other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self,other): #greater than #s1 > s2

        r1=self.m1+self.m2
        r2=other.m1+other.m2

        if(r1>r2):
            return True
        else:
            return False
        
    def __ge__(self,other): #greater than or equal to  #s1 >= s2
        r1=self.m1+self.m2
        r2=other.m1+other.m2
        if(r1>=r2):
            return True
        else:
            return False
        
        
    
    def __str__(self): #prints values in s3 by converting into string

        print("{} {}".format(s3.m1,s3.m2))  

s1=student(10,20)
s2=student(30,40)
s3=s1+s2
#in case of variables, on seeing "+", interpretor calls built-in  function __add__(a,b) which is defined for a+b
#but in this case (objects), s1+s2 calls our defined function in the class student (make sure both are of type student)

print(s3)
if(s1>s2): # calls __gt__
    print("s1")
else:
    print("s2")

if(s1>=s2): # calls __ge__
    print("s1 >= s1")
else:
    print("s2>s1")
    


    


    
