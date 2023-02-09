def has_33(nums): 
    for i in range(len(nums)): 
        if nums[i]==3: 
            if i+1 < len(nums) and nums[i+1]==3: 
                return True
    return False

numbers = list(map(int, input().split()))
print(has_33(numbers))