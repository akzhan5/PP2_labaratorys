def isPalindrome(word):
    check = ''
    i = len(word)-1
    while i>=0: 
        check+=word[i]
        i-=1
    if check == word: 
        return True
    else: return False

word = input()
print(isPalindrome(word))


