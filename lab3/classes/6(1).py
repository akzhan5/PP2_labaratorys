import math 

def isPrime(n): 
    if n==1: return False
    for i in range(2,int(math.sqrt(n) + 1)): 
        if (n%i==0): 
            return False
    return True

nums = list(map(int, input().split()))
primes = list(filter(lambda x: isPrime(x), nums)) 
#filter(function used for filter(lambda), list-iterable)
print('Primes are:',*primes)
