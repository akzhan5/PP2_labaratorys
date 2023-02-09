from mfs import apb
print(apb(2,3))

''' file from which function is imported should be in the same directory as 
a file calling them '''
from functions_used import to_ounce 
print(to_ounce(int(input())))

from functions_used import solve
print(solve(3,5))

from functions_used import filter_prime, reverse, has_33
print(filter_prime(list(map(int,input().split()))))
print(reverse('I respect you and me'))
print(has_33(list(map(int, input().split()))))

import functions_used
print(functions_used.isPalindrome('kaka'))
print()
print(functions_used.volume_sphere(9))


