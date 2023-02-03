#sort() - sort ascendingly list
thislist1 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist1.sort()
print(thislist1, '\n') #sorts alphanumerically

#sort the list numerically: 
thislist2 = [100,50,65,82,23]
thislist2.sort()
print(thislist2, '\n')

#sort descending: sort(reverse = True)
thislist3 = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist3.sort(reverse =True)
print(thislist3, '\n')

thislist4 = [100,50,65,82,23]
thislist4.sort(reverse = True)
print(thislist4, '\n')

#customize sort() using key = function
#sort the list based on how close the number is to 50
def func(n): 
    return abs(n-50) #number based on which the list will be sorted

thislist4.sort(key = func)
print(thislist4, '\n') #50(0) closest, 65(15), 23(23-50 = 27), 82(32), 100(50)

#case insensitive sort()(actually sort is case sensitive)
thislist5 = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist5.sort()
print(thislist5, '\n') #capitals first

#to get case insentisitive sort(key = str.lower)
thislist6 = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist6.sort(key = str.lower)
print(thislist6, '\n')

#Reverse Order (reverses the current list)
thislist7 = ['banana', 'Orange', 'Kiwi', 'cherry']
thislist7.reverse()
print(thislist7, '\n')







