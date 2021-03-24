from main import db, app, Pokemon
import csv

db.create_all(app=app)

# add code to parse csv, create and save pokemon objects

# with open('pokemon.csv', newline='') as csvfile:
#     pokemon = csv.reader(csvfile, delimiter=' ', quotechar='|')
#     for row in pokemon:
#         name = row["name"]
#         print(name)

with open('pokemon.csv', mode='r') as csv_file:
    Pokemons = csv.DictReader(csv_file)
    for pokemon in Pokemons:
        data = Pokemon(
            name = pokemon["name"]
            id = pokemon["id"], 
            attack = pokemon["attack"],
            defense =  pokemon["defense"],
            hp = pokemon["hp"],
            height = pokemon["height_m"],
            sp_attack = pokemon["sp_attack"],
            sp_defense = pokemon["sp_defense"],
            speed = pokemon["speed"],
            type1 = pokemon["type1"],
            type2 = pokemon["type2"],
            weight = pokemon['weight_kg']
        )
        print(data)
        db.session.add(data)
    db.session.commit()

# # with open('../data.json') as json_file:
#     data = json.load(json_file)
#     for pokemon in Pokemons:
#         data = Datas(
#             name = pokemon['name'],  
#             id = pokemon['id'], 
#             attack = pokemon['stats']['attack'],
#             defense =  pokemon['stats']['defense'],
#             hp = pokemon['stats']['hp'],
#             height = pokemon['physique']['height'],
#             sp_attack = pokemon['specials']['sp_attack'],
#             sp_defense = pokemon['specials']['sp_defense'],
#             speed = pokemon['stats']['speed'],
#             type1 = pokemon['type']['type1'],
#             type2 = pokemon['type']['type2'],
#             weight = pokemon['physique']['weight']
#         )
#         db.session.add(data)
#     db.session.commit()

# replace any null values with None to avoid db errors
