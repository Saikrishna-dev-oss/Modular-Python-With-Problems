square = lambda x :x**x
avg = lambda x,y,z :(x+y+z)/3
print(square(2))
print(avg(2,7,8))



def fibonacci(n):
    if (n==0 or n==1):
        return n
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter no: "))
for i in range(n):
    fib = fibonacci(i)
    print(fib,end = "\t")




def fact(n):
    if(n==0 or n==1):
        return 1
    return fact(n-1) * n
f = fact(5)
# print(f)
