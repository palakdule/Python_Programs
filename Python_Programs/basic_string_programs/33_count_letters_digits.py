text = "Python 3.10 is great!"

letter_count = 0
digit_count = 0

for char in text:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1

print(f"Text: {text}")
print(f"Letters: {letter_count}")
print(f"Digits: {digit_count}")
