str = str(input("Enter String: "))
revstr = str[::-1]
if(str == revstr):
    print("Palindrome")
else:
    print("Not Palindrome")



# COunt occurences of character in strings=

def count_char(text):
    char_count = {}

    for char in text :
        char_count[char] = char_count.get(char,0) + 1

    return char_count

text = input("Enter String: ")
text = text.replace(" ","")
char_counts = count_char(text)

for char,count in char_counts.items():
    print(f"{char} : {count}")




# extract word and sort alphabetically

import re 

def extract_word_sort(sentence):
    clean_sentence = re.sub(r'[^\w\s]', '', sentence)

    word_list = clean_sentence.split()

    sorted_list = sorted(word_list,key = str.lower)

    return sorted_list

sentence = "mango Apple Banana"
word_list = extract_word_sort(sentence)
print("Sorted Words:",word_list)
