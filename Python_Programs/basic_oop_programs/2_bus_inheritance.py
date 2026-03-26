class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

# Example usage
if __name__ == "__main__":
    school_bus = Bus("School Volvo", 180, 12)
    print(f"Vehicle Name: {school_bus.name}, Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")
