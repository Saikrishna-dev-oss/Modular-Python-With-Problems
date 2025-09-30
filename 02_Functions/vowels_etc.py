# COUNT VOWELS,CONSONENTS,ETC

def count_vowels_consonents_digits_spaces(text) :
    vowels = "aeiouAEIOU"
    special_char = "!@#$.*&^%?"
    vowels_count = consonent_count =  digits_count = spaces_count = special_char_count= 0

    for char in text :
        if char in vowels:
            vowels_count +=1
        elif char.isalpha() and char not in vowels:
            consonent_count +=1
        elif char.isdigit():
            digits_count +=1
        elif char.isspace():
            spaces_count +=1
        elif char in special_char:
            special_char_count +=1

    return vowels_count,consonent_count,digits_count,spaces_count,special_char_count


text = str(input("Enter a String: "))
vowels,consonents,digits,spaces,special_char = count_vowels_consonents_digits_spaces(text)
print(f"Number of Vowels = {vowels}")
print(f"Number of Consonents = {consonents}")
print(f"Number of Digits = {digits}")
print(f"Number of Spaces = {spaces}")
print(f"Number of Special Characters = {special_char}")