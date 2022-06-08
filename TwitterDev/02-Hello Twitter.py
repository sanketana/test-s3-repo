import requests
import json

header = {"Authorization" : "Bearer AAAAAAAAAAAAAAAAAAAAALcCZQEAAAAAP45Hk25w6MTAC7tVR%2BE94Ez8K1o%3DJp7o8K5S4mvb7wXOHiJaFcWOqeJWkDzNDBQdMHsKXBP8PXCDFF"}

base_url = 'https://api.twitter.com/'
api_endpoint = '2/tweets/search/recent?query=from%3Aelonmusk'

url = base_url + api_endpoint

response = requests.get(url, headers=header)

response_json = response.json()
print(json.dumps(response_json, indent=4))