def is_binary(s):
    for char in s:
        if char not in '01':
            return False
    return True

test1 = "10101"
test2 = "10201"

print(f"Is '{test1}' binary? {is_binary(test1)}")
print(f"Is '{test2}' binary? {is_binary(test2)}")
