from dict_of_movies import movies

def above(movie): 
    if movie['imdb']>5.5: 
        return True
    else: return False


for i in range(len(movies)): 
    print(movies[i]['name'], '-', above(movies[i]), end = '\n')


