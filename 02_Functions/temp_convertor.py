def convert_temp(value,scale):

    if (scale == "F" or scale == 'f'):
        return (9/5*value) + 32
    elif(scale == "C" or scale == 'c'):
        return (value - 32)*5/9
    else:
        print("please Enter a Valid Scale to Convert Temp")

value = int(input("Enter Temperature: "))
scale = input("Enter Scale for Conversion: ")

f = convert_temp(value,scale)
print(f)

