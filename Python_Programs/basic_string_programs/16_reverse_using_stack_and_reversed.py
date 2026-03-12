text = "Hello"

stack = list(reversed(text))

reversed_text = ""
while stack:
    reversed_text += stack.pop(0) # In this simple case, we just join them

traditional_stack = list(text)
rev_stack_result = ""
while traditional_stack:
    rev_stack_result += traditional_stack.pop()

print("Original:", text)
print("Reversed using stack-like logic:", rev_stack_result)
