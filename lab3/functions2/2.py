from dict_of_movies import movies

def sub_above(l): 
    good = []
    for i in range(len(movies)): 
        if movies[i]['imdb'] > 5.5: 
            good.append(movies[i]['name'])
    return good

print('Movies with imdb above 5.5:') 
print(*sub_above(movies), sep='\n')
