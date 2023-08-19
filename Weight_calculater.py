
class weight_calculater:
    def __init__(self,weight_on_earth,gravity_of_planet):#constuctor of class with 3 arguments
        self.weight=weight_on_earth                      #initializig two variables
        self.gravity=gravity_of_planet

    def calculate(self):  #Function to calculate weight
        weight=self.weight * self.gravity/9.8  #Formula

        print("The gravity of person on planet is:",weight,"N")

W=float(input("Enter the weight of person on Earth in kg: " )) #This line will get the weight of person on Earth in float or integer
g=float(input("Enter the gravity of planet on which you want to calculate the weight: "))#This line will get the gravity of desired planet from user 

obj=weight_calculater(W,g)

print(obj.calculate())

