#Method Overriding
class A:

    def show(self):
        print("A show")

class B(A):

    def show(self):
        print("B show")
a=B()
a.show()
        
#Here both classes A and B have same method show. B (child class) inherits A(parent class). When an object of child class(B)
#calls the method show, child class method is implemented not parent classs method.

#So it first checks B then goes to A
#This is happening because it is an object of class B, it checks it's class first.

#myopinion
#It is more like precedence.

#overriding meaning - more important than other or having dominance over other.



