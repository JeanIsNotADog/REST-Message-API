from flask import Flask
from flask_restful import Api, Resource
from flask_jwt import JWT
import sqlite3

from security import authenticate, identity
from resources.user import UserRegister
from resources.message import Message
from resources.check import Check

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///challenge.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.secret_key = 'xxxx'
api = Api(app)

@app.before_first_request
def create_tables():
	db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/login'

jwt = JWT(app, authenticate, identity)  
api.add_resource(UserRegister, '/users')
api.add_resource(Message, '/messages')
api.add_resource(Check, '/check')



if __name__ == '__main__':
	from db import db
	db.init_app(app)
	app.run(host='localhost', port=8080, debug=True)
