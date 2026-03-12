string1 = "hello"
string2 = "world"

common_chars = set(string1) & set(string2)

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print("Matched characters:", common_chars)
