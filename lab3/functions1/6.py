def reverse(string): 
    words = list(string.split())
    words.reverse()
    reversed_string = words
    return reversed_string   

string = input()
print(*reverse(string))

