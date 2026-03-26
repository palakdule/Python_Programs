class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

# Example usage
if __name__ == "__main__":
    car = Vehicle(240, 18)
    print(f"Max Speed: {car.max_speed}, Mileage: {car.mileage}")
