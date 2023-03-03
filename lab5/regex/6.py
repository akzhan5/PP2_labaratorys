import re 

string = input() 
repl = ":"
pattern = "[\s,.]" 

x = re.sub(pattern, repl, string)

print(x)
