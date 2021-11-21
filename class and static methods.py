""" METHODS
1. Instance method - works with object variables and takes self as an argument
2. Class method - works with class varibles and takes cls as an argument. Decorator "@classmethod" must be metioned before defining the method 
3. Static method - Use it when you don't work with class or object variables. Decorator "@staticmethod" must be metioned before defining the method 
"""

class school:

    school = "JGS"

    def __init__(self,name,gender,age):
        self.name=name;
        self.gender=gender
        self.age=age

    def  display(self):
        print("Name: ",self.name)
        print("Gender: ",self.gender)
        print("Age: ",self.age,"\n")

    @staticmethod
    def intro():
        print("Student details\n") 

    @classmethod
    def school_name(cls):
        print("They Belong to",cls.school) #accessing class var using cls

s=school("Amul","girl","10")
school.intro()
s.display()
school.school_name()

#class and static methods can be called with object name or class name
