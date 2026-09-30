def count_characters(text):
    vowels = 0
    consonants = 0
    digits = 0
    special_chars = 0
    
<<<<<<< HEAD
=======
    
>>>>>>> add766ae0aba7201c2c31a6ae2b40e1bcab771be
    vowel_set = "aeiouAEIOU"
    
    for char in text:
        if char.isdigit():
            digits += 1
        elif char.isalpha():
            if char in vowel_set:
                vowels += 1
            else:
                consonants += 1
        else:
<<<<<<< HEAD
           
=======
>>>>>>> add766ae0aba7201c2c31a6ae2b40e1bcab771be
            special_chars += 1
            
    return vowels, consonants, digits, special_chars

input_string = "Hello World! Welcome to Python 2026. #Code"
v, c, d, s = count_characters(input_string)

print(f"Input String: {input_string}\n")
print(f"Vowels: {v}")
print(f"Consonants: {c}")
print(f"Digits: {d}")
print(f"Special Characters: {s}")
