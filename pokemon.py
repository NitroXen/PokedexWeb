import requests


def get_pokemon_filter(name):
    url = f"https://pokeapi.co/api/v2/pokemon/?limit=649"

    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        response = response.json()
    result = response['results']
    total = []
    img = []
    for r in result:
        if r['name'].lower().find(name.lower()) != -1:
            total.append(r['name'])
        num = r['url'].split()[len(r['url'].split())-2]
        img.append(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{num}.png")
    
    
    return total, img



def get_pokemon_list():
    url = 'https://pokeapi.co/api/v2/pokemon/?limit=649'
    response = requests.get(url).json()
    result = response['results']
    img = []
    for i in range(len(result)):
        img.append(f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{i+1}.png")
    return result, img


def pokemon_info(i):
    url = f"https://pokeapi.co/api/v2/pokemon-species/{i}"

    response = requests.get(url)
    response.raise_for_status()
    if response.status_code == 200:
        response = response.json()
        
    img = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/other/official-artwork/{response['id']}.png"



    return response, img
