chars = ['a', 'b', 'c', 'd', 'e']
n = len(chars)
for i in range(n // 2):
    chars[i], chars[n - 1 - i] = chars[n - 1 - i], chars[i]
print(chars)
