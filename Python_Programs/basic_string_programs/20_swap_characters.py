text = "python"
text_list = list(text)

text_list[0], text_list[-1] = text_list[-1], text_list[0]

swapped_text = "".join(text_list)

print("Original: python")
print("Swapped (first and last):", swapped_text)
