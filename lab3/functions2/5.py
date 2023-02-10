from dict_of_movies import movies

def InCategoryAverage(c): 
    sum =0
    cnt=0
    for i in range(len(movies)): 
        if movies[i]['category'] == c: 
            sum+=movies[i]['imdb']
            cnt+=1
    return round(sum/cnt, 2)

c = input()
print(InCategoryAverage(c))


