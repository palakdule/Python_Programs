total_sum = 0
with open("numbers.txt", "r") as file:
    for line in file:
        total_sum += float(line.strip())
print(total_sum)
