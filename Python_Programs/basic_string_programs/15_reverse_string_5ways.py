text = "Python"

rev1 = text[::-1]
print("Way 1 (Slicing):", rev1)

rev2 = "".join(reversed(text))
print("Way 2 (reversed()):", rev2)

rev3 = ""
for char in text:
    rev3 = char + rev3
print("Way 3 (Loop):", rev3)

rev4 = ""
i = len(text) - 1
while i >= 0:
    rev4 += text[i]
    i -= 1
print("Way 4 (While Loop):", rev4)

def reverse_recursive(s):
    if len(s) == 0:
        return s
    else:
        return reverse_recursive(s[1:]) + s[0]

print("Way 5 (Recursion):", reverse_recursive(text))
