text = "hello world python"

words = text.split()

camel_case = words[0].lower() + "".join(word.capitalize() for word in words[1:])

print("Original:", text)
print("camelCase:", camel_case)
