text = "Python is a great language for beginners"

words = text.split()

print("Even length words are:")
for word in words:
    if len(word) % 2 == 0:
        print(word)
