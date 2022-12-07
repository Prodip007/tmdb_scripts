import requests
import json

f = open('movie_list.txt', 'r')

moviename_lines = f.readlines()
movies = []
new_movies = []

for line in moviename_lines:
    movies.append(line.strip())

for movie in movies:
    x = movie.replace(' ', '+')
    new_movies.append(x)



for movie in new_movies:
    res_json = requests.get('https://api.themoviedb.org/3/search/movie?api_key=75d0735db2c040c342d1d72122fb9043'+'&query='+movie)
    res = json.loads(res_json.content)

    new_list = res['results']
    new_dict = new_list[0]
    current_id= new_dict['id']
    print(current_id)

