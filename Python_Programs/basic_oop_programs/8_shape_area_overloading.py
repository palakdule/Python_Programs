import math

class ShapeArea:
    def area(self, *args):
        n = len(args)
        if n == 1:
            # Square (side)
            return args[0] ** 2
        elif n == 2:
            # Rectangle (length, width) or Ellipse (a, b)
            # We'll use a type check or separate logic if needed, but the prompt implies overloading.
            # Let's assume (length, width) for rectangle
            return args[0] * args[1]
        elif n == 3:
            # Triangle (base, height, 'triangle')
            if args[2] == 'triangle':
                return 0.5 * args[0] * args[1]
        return "Invalid arguments"

    def circle_area(self, radius):
        return math.pi * radius ** 2

    def ellipse_area(self, a, b):
        return math.pi * a * b

# In Python, we can simulate overloading with default arguments or *args
def find_area(shape, *args):
    if shape.lower() == 'square':
        return args[0] ** 2
    elif shape.lower() == 'rectangle':
        return args[0] * args[1]
    elif shape.lower() == 'triangle':
        return 0.5 * args[0] * args[1]
    elif shape.lower() == 'circle':
        return math.pi * args[0] ** 2
    elif shape.lower() == 'ellipse':
        return math.pi * args[0] * args[1]
    else:
        return "Unknown shape"

if __name__ == "__main__":
    print(f"Area of Square (side=5): {find_area('square', 5)}")
    print(f"Area of Rectangle (5, 10): {find_area('rectangle', 5, 10)}")
    print(f"Area of Triangle (base=5, height=10): {find_area('triangle', 5, 10)}")
    print(f"Area of Circle (radius=7): {find_area('circle', 7):.2f}")
    print(f"Area of Ellipse (a=5, b=3): {find_area('ellipse', 5, 3):.2f}")
