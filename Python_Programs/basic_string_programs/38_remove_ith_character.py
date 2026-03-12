text = "Python"
i = 3 # Removing 'h' at index 3

new_text = text[:i] + text[i+1:]

print(f"Original: {text}")
print(f"After removing character at index {i}: {new_text}")
