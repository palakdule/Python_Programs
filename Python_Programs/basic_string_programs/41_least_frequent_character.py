text = "apple"

freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1

least_freq_char = min(freq, key=freq.get)

print(f"The least frequent character in '{text}' is: '{least_freq_char}'")
