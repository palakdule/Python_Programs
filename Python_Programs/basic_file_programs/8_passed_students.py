with open('grades.txt', 'r') as infile, open('passed.txt', 'w') as outfile:
    for line in infile:
        name, grade = line.strip().rsplit(' ', 1)
        if grade in ['A', 'B']:
            outfile.write(name + '\n')