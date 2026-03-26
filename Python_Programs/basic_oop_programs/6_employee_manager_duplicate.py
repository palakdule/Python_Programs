class Employee:
    def __init__(self, name=None, age=None, salary=None, address=None):
        self.name = name
        self.age = age
        self.salary = salary
        self.address = address

    def get_input(self):
        self.name = input("Enter name: ")
        self.age = input("Enter age: ")
        self.salary = input("Enter salary: ")
        self.address = input("Enter address: ")

    def print_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Salary: {self.salary}, Address: {self.address}")

class Manager(Employee):
    pass

# Process information for 10 managers
if __name__ == "__main__":
    managers = []
    print("Processing info for 10 managers:")
    for i in range(1, 11):
        print(f"\nEnter details for Manager {i}:")
        m = Manager()
        m.get_input()
        managers.append(m)

    print("\n--- Manager Information ---")
    for m in managers:
        m.print_info()
