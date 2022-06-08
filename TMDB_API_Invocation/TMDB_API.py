import requests
import json

# Search API Example: https://api.themoviedb.org/3/search/movie?api_key={api_key}&query=Jack+Reacher
# Movie API Example: https://api.themoviedb.org/3/movie/238?api_key={api_key}

api_url = 'https://api.themoviedb.org/3/'
api_name = 'movie/'
movie_id = '238'
api_key = 'f7caef429cefd379e4cc73927f6be227'


api_call = api_url + api_name + movie_id + "?api_key=" + api_key

response = requests.get(api_call)
response_dict = response.json()

print(json.dumps(response_dict, indent=4))
#print(api_call)