def histogram(nums): 
    for i in nums: 
        print('*'* i)

l = list(map(int, input().split()))
histogram(l)