

def largest(a,b,c):
    if a>b and a>c:
        return a
    elif b>c:
        return b
    else :
        return c 
# a = int(input("Enter Number 1 : "))
# b = int(input("Enter Number 2 : "))
# c = int(input("Enter Number 3 : "))
# largest_num = largest(a,b,c)
# print(largest_num)


#celcius to Fahrenheit

def celcius_fahrenheit(c):
    f = (9/5*c)+32;
    return f
# c = int(input("Enter Temperature in Celcius : "))
# f = celcius_fahrenheit(c)
# print(f)


# Fahrenheit to celcius

def fahrenheit_celcius(f):
    c = (5/9)*(f-32);
    return c
# f = int(input("Enter Temperature in fahrenheit : "))
# c = fahrenheit_celcius(f)
# print(c)



# for i in range(1,101):
#     if(i%3 == 0 and i%5 == 0) :
#         print("Fizz Buzz")
#     elif i%3 == 0 :
#         print("Fizz")
#     elif i%5 == 0 :
#         print("Buzz")
#     else:
#         print(i)

# Prime number

def is_prime(n) :
    for i in range(2,int(n**0.5) + 1) :
        if(n%i == 0):
            return False    
        else :
            return True

num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")


# Fibonacci

# f1 = 0
# f2 = 1
# num = int(input("Enter a number: "))
# print(f1,"\t",f2,end = "\t")
# for i in range(num) :
#     f3 = f1 + f2
#     print(f3, end = "\t")
#     f1 = f2
#     f2 = f3 


# NUmber of vowels in string

def count_vowels_consonents_digits_spaces_special_char(text) :
    vowels = "aeiouAEIOU"
    special_char = "!@#$.*&^%?"
    vowels_count = consonent_count =  digits_count = spaces_count = special_char_count = 0

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
vowels,consonents,digits,spaces,special_char = count_vowels_consonents_digits_spaces_special_char(text)
print(f"Number of Vowels = {vowels}")
print(f"Number of Consonents = {consonents}")
print(f"Number of Digits = {digits}")
print(f"Number of Spaces = {spaces}")
print(f"Number of Special Characters = {special_char}")




