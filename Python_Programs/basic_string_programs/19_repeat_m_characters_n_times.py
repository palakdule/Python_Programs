text = "Programming"
M = 3 # Number of characters from the start
N = 4 # Number of repetitions

substring = text[:M]

result = substring * N

print(f"Repeating first {M} characters {N} times: {result}")
