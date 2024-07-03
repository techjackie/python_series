"""
class class_name:
    logic
"""

class BMW:
    color = "black"
    seat = 4
    variant = "BMW X1"
    name = "BMW"

    def start(self):
        print(self.name," is Starting On..")

    def stop(self):
        print("Car is Stopped!")    
    

# object = class_name()
car1 = BMW()
car2 = BMW()
car3 = BMW()

# obj.variable_Name
car1.color = "red"
car2.color = "green"

car1.name = "Car 1"
car2.name = "Car 2"

# obj.function_name()
car1.start()
car2.start()

