def to_ounce(grams): 
    return grams * 28.3495231

def to_centrigade(farenheit): 
    C = (5 / 9) * (farenheit - 32)
    print(C)

def solve(numheads, numlegs): 
    '''c + r = numheads 
    2*c + 4*r = numlegs
    2*r = numlegs - 2*numheads'''
    r = int((numlegs - 2*numheads)/2)
    c = int(numheads - r)
    print('The number of rabbits: ', r)
    print('The number of chickens: ', c)

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

def reverse(string): 
    words = list(string.split())
    words.reverse()
    reversed_string = words
    return reversed_string   

def has_33(nums): 
    for i in range(len(nums)): 
        if nums[i]==3: 
            if i+1 < len(nums) and nums[i+1]==3: 
                return True
    return False

def spy_game(nums): 
    spy = ''
    if nums.count(0)!=2 or nums.count(7)!=1: 
        return False
    else: 
        for i in nums: 
            if i==0 or i==7: 
                spy+=str(i)
    if spy=='007': 
        return True
    else: 
        return False

def volume_sphere(radius): 
    vol = (4*3.14*pow(radius, 3))/3
    print(vol)

def unique(lis): 
    uni = []
    for i in range(len(lis)): 
        if lis.count(lis[i])==1: 
            uni.append(lis[i])
    return uni

def isPalindrome(word):
    check = ''
    i = len(word)-1
    while i>=0: 
        check+=word[i]
        i-=1
    if check == word: 
        return True
    else: return False

def histogram(nums): 
    for i in nums: 
        print('*'* i)

