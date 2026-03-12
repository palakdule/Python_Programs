text = "Python is a high level programming language"
k = 5

words = text.split()
result = []

for word in words:
    if len(word) > k:
        result.append(word)

print(f"Words greater than length {k}:", result)
