import re

text = "My contact number is 9876543210. Please call me."

mobile_number = re.search(r'\d{10}', text)

if mobile_number:
    print("Extracted Mobile Number:", mobile_number.group())
else:
    print("No mobile number found.")
