import re
details = "Email:krishna003@gmail.com,phno:6305689287,damn"
text3 = "Hello, world! It's a beautiful day."
type1 = re.sub(r'\d','*',details)
type2 = re.sub(r'\bdamn\b','****',details,flags=re.IGNORECASE)
type3 = re.sub(r'[^\w\s]', '', text3)

print(type1)
print(type2)
print(type3)

def mini_sub_digit(txt,replacement = '*'):
    result = ''
    for char in text:
        if char.isdigit():
            result +=replacement
        else:result += char
    return result
text = "Email:krishna003@gmail.com,phno:6305689287"
updated_text = mini_sub_digit(text)
print(updated_text)