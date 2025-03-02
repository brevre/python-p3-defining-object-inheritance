# Import the Vehicle class from vehicle.py
from vehicle import Vehicle

# Define the Car class, inheriting from Vehicle
class Car(Vehicle):
    # Overriding the go() method from Vehicle
    def go(self):
        return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
