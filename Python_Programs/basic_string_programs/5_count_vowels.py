text = "Hello Everyone"

vowels = "aeiouAEIOU"

count = 0

for char in text:
    if char in vowels:
        count += 1

print("Number of vowels in the string:", count)
