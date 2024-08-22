class Vehicle:
    def __init__(self, number_of_wheels, paint_color, seating_capacity, maximum_velocity):
        self.number_of_wheels = number_of_wheels
        self.paint_color = paint_color
        self.seating_capacity = seating_capacity
        self.maximum_velocity = maximum_velocity

# Instantiating the Vehicle class
tesla_model_s = Vehicle(4, 'red', 6, 250)

# You can print the attributes to verify
print(f"Tesla Model S: {tesla_model_s.number_of_wheels} wheels, {tesla_model_s.paint_color} color, seating capacity {tesla_model_s.seating_capacity}, max velocity {tesla_model_s.maximum_velocity} km/h")
