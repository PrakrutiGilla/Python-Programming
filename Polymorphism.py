class A:

    def sho(self):
        print("A show")

class C:
    def sho(self):
        print("c show")
        

class B(A,C):

    def show(self):
        print("B show")
        C.sho(self)

    
a=B()
a.show()
        
        


