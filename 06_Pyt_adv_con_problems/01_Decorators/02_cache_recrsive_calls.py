import time 
def cache_fibnocci(func) :
    cache = {}              #Memory bank to store results for increasing n

    def wrapper(n):
        if n in cache :         #checks if data in cache
            return cache[n]
        result = func(n)        #Compute n value if not in cache
        cache[n] = result       #Save result for future use
        return result
    return wrapper
@cache_fibnocci
def fibnocci(n):
    if(n==0 or n==1):
        return n
    else:
        return fibnocci(n-1) + fibnocci(n-2)
    
n = int(input("Enter num:"))
result = fibnocci(n)
start = time.time()
result = fibnocci(n)
end = time.time()
print(f"Execution time is : {end-start:.5f}")
print(f"Result :{result}")
    