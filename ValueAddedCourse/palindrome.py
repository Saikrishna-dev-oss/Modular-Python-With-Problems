def palindrome(str1) :
    revstr = str1[::-1]
    if(str1 == revstr):
        print("Palindrome")
    else :
        print("Not a Palindrome")


str1 = str(input("Enter the Value: "))
palindrome(str1)
