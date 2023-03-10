s = input() 
s1 = reversed(s)
s2 = ''

for i in s1: 
    s2+=i

if s == s2: 
    print('String is a palindrome')
else: 
    print('String is not a palindrome')


