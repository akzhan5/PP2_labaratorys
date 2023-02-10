import random 

print('Hello! What is your name?', end='\n')
name = input()
#randrange() - returns the given number in a range of start and end 
numb = random.randrange(1,20)
print('Well, ' + name + ', I am thinking of a number between 1 and 20.') 
print('Take a guess')
guess = int(input())
cnt =0
while guess != numb: 
    cnt+=1
    if guess > numb: 
        print('Your guess is too high.') 
        print('Take a guess')
        guess = int(input())
    elif guess < numb: 
        print('Your guess is too low.')
        print('Take a guess')
        guess = int(input())
else: 
    cnt+=1
    print('Good job, ' + name+ '! You guessed my number in ' +str(cnt) + ' guesses!')







