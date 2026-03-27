names = ['Alice', 'Bob', 'Charlie']
with open('names.txt', 'w') as file:
    for name in names:
        file.write(name + '\n')