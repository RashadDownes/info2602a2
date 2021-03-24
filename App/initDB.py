from main import db, app #, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects

with open('./data.json') as json_file:
    data = json.load(json_file)
    for pokemon in Pokemons:
        data = Datas(
            name = pokemon['name'],  
            id = pokemon['id'], 
            attack = pokemon['stats']['attack']
            defense =  pokemon['stats']['defense']
            hp = pokemon['stats']['hp']
            height = pokemon['physique']['height']
            sp_attack = pokemon['specials']['sp_attack']
            sp_defense = pokemon['specials']['sp_defense']
            speed = pokemon['stats']['speed']
            type1 = pokemon['type']['type1']
            type2 = pokemon['type']['type2']
            weight = pokemon['physique']['weight']
        )
        db.session.add(data)
    db.session.commit()

# replace any null values with None to avoid db errors
