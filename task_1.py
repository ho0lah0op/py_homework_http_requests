import requests
import json

urls = [
    f'https://akabab.github.io/superhero-api/api/id/332.json',
    f'https://akabab.github.io/superhero-api/api/id/149.json',
    f'https://akabab.github.io/superhero-api/api/id/655.json',
]

def requests_get(url_all):
    r = (json.loads(requests.get(url).text) for url in url_all)
    return r

def parser():
    temp_intelligence = 0
    for item in requests_get(urls):
        superhero_intelligence = item['powerstats']['intelligence']
        if superhero_intelligence > temp_intelligence:
            superhero_name = item['name']
            temp_intelligence = superhero_intelligence
    print(f'Самый умный супергерой: {superhero_name}, его интеллект: {temp_intelligence}')

parser()
