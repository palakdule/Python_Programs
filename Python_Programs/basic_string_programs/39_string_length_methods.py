text = "Hello"

len1 = len(text)
print("Way 1 (len()):", len1)

len2 = 0
for char in text:
    len2 += 1
print("Way 2 (Loop):", len2)

len3 = 0
while text[len3:]:
    len3 += 1
print("Way 3 (While Loop):", len3)
