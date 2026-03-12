data = [2, 23, 24, 51, 46, 67]
even = [x for x in data if x % 2 == 0]
odd = [x for x in data if x % 2 != 0]
print("Even", even)
print("Odd", odd)
