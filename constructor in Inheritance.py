#constructor in Inheritance

""" Remove hashes and check the output"""

class A(): # Here init method is constructor as it is used to declare and store variables

    def __init__(self):
        print("In init A")

    def module1():
        print("module 1")

class B(A):

    

    def __init__(self):
      # super().__init__() [ this step will make it print both - In init A and In init B ]
        print("In init B")

    def module1():
        print("module 1")


b=B()
"""output - in init B. This implies even though it has 2 constructors - class A and B.
It first checks for init of B and will print the variables in it first."""

class C(A,B):
   
                         #MRO - Method Resolution Order
    def __init__(self):
      # super().__init__() [ this step will make it print  - In init A and In init C ]
        print("In init C")

        """Here it had 2 super(parent) classes - A and B. It chose to print init of A (not B)
          as it goes with left first and then comes to right. This is known as MRO.(flow from left to right)."""
