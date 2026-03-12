text = "banana"

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

max_char = max(freq, key=freq.get)

print(f"The maximum frequency character in '{text}' is: '{max_char}'")
