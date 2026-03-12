text = "Hello"
index_to_remove = 2 # Removing 'l' at index 2

new_text = text[:index_to_remove] + text[index_to_remove + 1:]

print(f"Original: {text}")
print(f"After removing index {index_to_remove}: {new_text}")
