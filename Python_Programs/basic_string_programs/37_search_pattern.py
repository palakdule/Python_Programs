import re

text = "The rain in Spain falls mainly in the plain."
pattern = "Spain"

match = re.search(pattern, text)

if match:
    print(f"Pattern '{pattern}' found at index {match.start()}.")
else:
    print(f"Pattern '{pattern}' not found.")
