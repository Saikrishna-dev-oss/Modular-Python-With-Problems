
# Fibonacci 

def fib(num):
    if(num == 0 or num == 1):
        return num
    else:
        return fib(num-2) + fib(num-1)
num = int(input("Enter the Nth Fibonaaci Number :"))
for i in range(0,num):
    fib_Num = fib(i)
    print(fib_Num,end = "\t")