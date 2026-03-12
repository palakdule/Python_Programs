text = "abc"
length = len(text)

total_substrings = int(length * (length + 1) / 2)

print(f"The string '{text}' has {total_substrings} possible substrings.")
