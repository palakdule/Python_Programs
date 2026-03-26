def student_data(student_id, **kwargs):
    print(f"Student ID: {student_id}")
    if 'student_name' in kwargs:
        print(f"Student Name: {kwargs['student_name']}")
    if 'student_class' in kwargs:
        print(f"Student Class: {kwargs['student_class']}")

# Example usage
if __name__ == "__main__":
    print("Example 1:")
    student_data(101)
    print("\nExample 2:")
    student_data(102, student_name="David")
    print("\nExample 3:")
    student_data(103, student_name="Alice", student_class="Grade 10")
