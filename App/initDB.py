from main import db, app, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects
with open('pokemon.csv', mode='r') as csv_file:
    pokemonFile = csv.DictReader(csv_file)
    # replace any null values with None to avoid db errors
    for pokemon in pokemonFile:
        if pokemon["attack"] == '':
            pokemon["attack"] = None
        if pokemon["defense"] == '':
            pokemon["defense"] = None
        if pokemon["hp"] == '':
            pokemon["hp"] = None
        if pokemon["height_m"] == '':
            pokemon["height_m"] = None
        if pokemon["sp_attack"] == '':
            pokemon["sp_attack"] = None
        if pokemon["sp_defense"] == '':
            pokemon["sp_denfese"] = None
        if pokemon["speed"] == '':
            pokemon["speed"] = None
        if pokemon["type2"] == '':
            pokemon["type2"] = None
        if pokemon["type2"] == '':
            pokemon["type2"] = None
        if pokemon["weight_kg"] == '':
            pokemon["weight_kg"] = None
        
        pokemons = Pokemon(
            pid = pokemon["pokedex_number"], 
            name = pokemon["name"],
            attack = pokemon["attack"],
            defense =  pokemon["defense"],
            hp = pokemon["hp"],
            height = pokemon["height_m"],
            sp_attack = pokemon["sp_attack"],
            sp_defense = pokemon["sp_defense"],
            speed = pokemon["speed"],
            type1 = pokemon["type1"],
            type2 = pokemon["type2"],
            weight = pokemon["weight_kg"]
        )
        print(pokemons)
        db.session.add(pokemons)
    db.session.commit()


