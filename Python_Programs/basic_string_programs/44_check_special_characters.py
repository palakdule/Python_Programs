import re

def has_special_char(s):
    if re.search(r'[^a-zA-Z0-9\s]', s):
        print(f"'{s}' contains special characters.")
    else:
        print(f"'{s}' has no special characters.")

has_special_char("Hello World!")
has_special_char("Python123")
