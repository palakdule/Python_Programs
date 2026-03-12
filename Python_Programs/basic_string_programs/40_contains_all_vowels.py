def check_all_vowels(s):
    vowels = set("aeiou")
    s_vowels = set(char.lower() for char in s if char.lower() in vowels)
    
    if s_vowels == vowels:
        print(f"'{s}' contains all vowels.")
    else:
        print(f"'{s}' does NOT contain all vowels.")

check_all_vowels("education")
check_all_vowels("hello")
