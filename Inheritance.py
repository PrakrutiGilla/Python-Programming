#inheritance

class A:

    def module1(self):
        print("module 1 is working")

    def module2(self):
        print("module 2 is working")

class B(A):  #single-level Inheritance -(inherits properties of class A)- Therefore object of class B can call all methods of class A

    def module3(self):
        print("module 3 is working")

    def module4(self):
        print("module 4 is working")
        A.module1(self) #calling parents class
        
   
        
     
class C(B):  #multilevel-inheritance (Since B has inherited properties of A. C gets properties of both A and B)

    def module5(self):
        print("module 5 is working")
        A.module1(self) #calling Super class

class D:

     def module6(self):
         print("module 6 is working")


class E(A,D): #multiple inheritance (A and D are different classes. So it is called multiple. Class E inherits A and D)

     def module7(self):
         print("module 7 is working")

a=B()
a.module1()

b=C()
b.module1()
b.module3()

c=E()
c.module6()

a=C()
a.module5()
