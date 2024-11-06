class Bicycle:
    # Constructor to initialize properties
    def __init__(self, color, bike_type):
        self.color = color
        self.bike_type = bike_type

    # Method to simulate pedaling
    def pedal(self):
        print(f"The {self.color} {self.bike_type} is pedaling!")

    # Method to simulate braking
    def brake(self):
        print(f"The {self.color} {self.bike_type} has stopped.")

# Main code to create an instance and use its methods
if __name__ == "__main__":
    # Instance creation
    my_bike = Bicycle("Blue", "Mountain Bike")

    # Using object methods
    my_bike.pedal()
    my_bike.brake()
