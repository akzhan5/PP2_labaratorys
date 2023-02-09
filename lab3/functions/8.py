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

l = list(map(int, input().split()))
print(spy_game(l))