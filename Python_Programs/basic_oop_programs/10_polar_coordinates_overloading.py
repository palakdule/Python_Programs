import math

class Polar:
    def __init__(self, radius, angle_degrees):
        self.radius = radius
        self.angle = angle_degrees # angle in degrees

    def __add__(self, other):
        # Convert to rectangular
        x1 = self.radius * math.cos(math.radians(self.angle))
        y1 = self.radius * math.sin(math.radians(self.angle))
        
        x2 = other.radius * math.cos(math.radians(other.angle))
        y2 = other.radius * math.sin(math.radians(other.angle))
        
        # Add rectangular coordinates
        x_res = x1 + x2
        y_res = y1 + y2
        
        # Convert back to polar
        r_res = math.sqrt(x_res**2 + y_res**2)
        a_res = math.degrees(math.atan2(y_res, x_res))
        
        return Polar(r_res, a_res)

    def __str__(self):
        return f"Polar(Radius: {self.radius:.2f}, Angle: {self.angle:.2f}°)"

if __name__ == "__main__":
    p1 = Polar(10, 30)
    p2 = Polar(10, 60)
    
    p3 = p1 + p2
    print(f"Point 1: {p1}")
    print(f"Point 2: {p2}")
    print(f"Result (P1 + P2): {p3}")
