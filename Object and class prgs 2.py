#converting celsius to fahrenheit
"""class temperature:

    def __init__(self,temp):
        self.temp=temp

    def fahrenheit(self):
        return (self.temp*(9/5))+32

    def celsius(self):
        return (self.temp-32)*(5/9)

t=temperature(32)
print(t.celsius()) """

# OR

"""class temperature:
    
  def  convertFahrenhiet(self,celsius):
    return (celsius*(9/5))+32
  def convertCelsius(self,farenhiet):
    return (farenhiet-32)*(5/9)

t=temperature()
print(t.convertCelsius(32)) """

# display student name and roll.no, assign marks
"""class student:

    def __init__(self,name,roll_no):
        self.name=name
        self.roll_no=roll_no

    def display(self):
        print("name = {0}  roll.no = {1}".format(self.name,self.roll_no))

    def set_age(self,age):
        print(age)

    def set_marks(self,marks):
        self.marks=marks  #assigning marks to the student

s=student("amul",515)
s.display()
s.set_age(23)"""

# to take input from user
"""class age:

    def user(self):
        n=int(input("enter age"))
        self.age=n
        return self.age + 20

i=age()
print(i.user())"""
        
