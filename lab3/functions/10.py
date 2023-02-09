def unique(lis): 
    uni = []
    for i in range(len(lis)): 
        if lis.count(lis[i])==1: 
            uni.append(lis[i])
    return uni

l_inp = list(input().split())
print(unique(l_inp))

