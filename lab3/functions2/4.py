from dict_of_movies import movies

def average(list): 
    sum_imdb =0
    for i in range(len(list)): 
        sum_imdb+=list[i]['imdb']
    return (sum_imdb/len(list))

print(round(average(movies), 2))

