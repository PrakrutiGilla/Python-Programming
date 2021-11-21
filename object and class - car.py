class car:

   def __init__(self,colour,model,fuel_tank_cc,speed):
        self.colour=colour
        self.model=model
        self.fuel_tank_cc=fuel_tank_cc
        self.speed=speed

   def display(self):

       print("Color: {}, model: {}, tank cc: {}, speed: {}".format(self.colour,self.model,self.fuel_tank_cc,self.speed))

Indica=car("red","hatchback","20 litres","200km/hr")
Indica.display()
