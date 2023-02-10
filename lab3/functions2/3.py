from dict_of_movies import movies


def InCategory(c): 
    mov = []
    for i in range(len(movies)): 
        if movies[i]['category'] == c: 
            mov.append(movies[i]['name'])
    return mov 


cat = input()
print(*InCategory(cat), sep='\n')


