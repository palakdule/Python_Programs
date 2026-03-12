var1 = "Hello"
var2 = 123

def check_if_string(var):
    if isinstance(var, str):
        print(f"'{var}' is a string.")
    else:
        print(f"'{var}' is NOT a string.")

check_if_string(var1)
check_if_string(var2)
