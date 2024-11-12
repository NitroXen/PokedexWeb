from flask import Flask,request, render_template, redirect
from pokemon import get_pokemon_list, pokemon_info, get_pokemon_filter
import random

app = Flask(__name__)

@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


@app.route('/search', endpoint='?q={pokem}', methods=['GET'])
def search():
    p = request.args.get('q')

    poke, img= get_pokemon_filter(p)
    


    return render_template('filter.html', pokemons=poke, img= img)

@app.route('/pokemon/<index>')
def pokemon(index):

    poke, img= pokemon_info(index)

    text = []
    for i in poke['flavor_text_entries']:
        if i['language']['name'] == 'es':
            text.append(i['flavor_text'])


    return render_template('pokemon.html', pokemon = poke['name'], info = random.choice(text), img = img)

@app.route('/', methods=['GET'])
def index():
    poke, img = get_pokemon_list()

    pokemons = []
    for i in poke:
        pokemons.append(i['name'])

    return render_template('index.html', pokemons=pokemons, img = img)



if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")