import math

nums = list(map(int, input().split()))

primes = list(filter(lambda x: all(x%i != 0 for i in range(2, int(math.sqrt(x))+1)), nums))

print(*primes)