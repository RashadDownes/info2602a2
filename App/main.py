import json
import jinja2
from flask import Flask, request, render_template
from flask_jwt import JWT, jwt_required, current_identity
from sqlalchemy.exc import IntegrityError
from datetime import timedelta 

from models import db , User, Pokemon, MyPokemon

''' Begin boilerplate code '''
def create_app():
  app = Flask(__name__, static_url_path='')
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
  app.config['SECRET_KEY'] = "MYSECRET"
  app.config['JWT_EXPIRATION_DELTA'] = timedelta(days = 7) 
  db.init_app(app)
  return app

app = create_app()

app.app_context().push()

''' End Boilerplate Code '''

''' Set up JWT here '''
headings = ("Name", "Type1", "Type2", "Weight", "Height")
data = Pokemon(
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
''' End JWT Setup '''

# edit to query 50 pokemon objects and send to template
@app.route('/')
def index():
  return render_template('index.html', headings = headings, data = data)


@app.route('/app')
def client_app():
  return app.send_static_file('app.html')


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080, debug=True)