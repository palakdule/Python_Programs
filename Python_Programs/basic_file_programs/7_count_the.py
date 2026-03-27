with open('words.txt', 'r') as file:
    content = file.read().lower()
    count = content.split().count('the')
    print(count)