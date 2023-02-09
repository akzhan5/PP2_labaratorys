def filter_prime(numbers): 
    isPrime = True
    primes =[]
    for i in numbers: 
        for j in range(2, int(i/2)): 
            if i%j==0: 
                isPrime = False
        if isPrime == True and i!=1: 
            primes.append(i)
        isPrime = True
    if len(primes)==0: 
        return 'No primes in the list'
    else: 
        return primes

nums = list(map(int, input().split()))
print(*filter_prime(nums))