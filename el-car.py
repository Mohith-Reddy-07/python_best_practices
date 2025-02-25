class vehicle:
    def display_type(self):
        print("this is a vehicle")

class car(vehicle):
    def __init__(self,brand):
        self.brand = brand
        
    def display_brand(self):
        print(f"car brand: {self.brand}")
        
class electriccar(car):
    def __init__(self,brand,battery):
        super().__init__(brand)
        self.battery = battery
        
    def display_battery(self):
        print(f"battery capacity: {self.battery}kwh")
        
ev = electriccar("Tesla",250)
ev.display_type()
ev.display_brand()
ev.display_battery()