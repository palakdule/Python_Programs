class Student:
    def __init__(self, student_name, marks):
        self.student_name = student_name
        self.marks = marks

# Example usage
if __name__ == "__main__":
    s1 = Student("John Doe", 85)
    print(f"Original Values: Name = {s1.student_name}, Marks = {s1.marks}")
    
    # Modifying attributes
    s1.student_name = "Jane Smith"
    s1.marks = 92
    print(f"Modified Values: Name = {s1.student_name}, Marks = {s1.marks}")
