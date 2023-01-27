#use \ - to prevent errors for characters not used there

''' txt = 'We are 'vikings' from the north'  error '''

#sol: 
txt = 'We are \'Vikings\' from he north'

#escape chars: 
txt = 'It\'s alright.'
print(txt)

txt = 'This will insert one \\ (backlash)'
print(txt)

txt = 'Hello\nWorld' #n- new line read with \n
print(txt, '\n')

#carriage return 
txt  = 'Hello\rWorld'
print(txt)

#tab - adds tab 
txt = 'Hello\tWorld'
print(txt)

#backspace \b -erases on back char
txt = 'Hello\bWorld'
print(txt)

#form feed 
txt = 'Hello\fWorld'

#\3ints - octal value 
txt = '\110\145\154\154\157'
print(txt)

#xhh - hexodec val
txt = '\x48\x65\x6c\x6f'
print(txt)

