from flask_restful import Resource, reqparse
from models.user import UserModel
from datetime import datetime


class UserRegister(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('username',
						type=str,
						required=True
	)
	parser.add_argument('password',
						type=str,
						required=True
	)

	def post(self):
		data = UserRegister.parser.parse_args()

		if UserModel.find_by_username(data['username']):
			return {'message': 'A user with this username already existed'}, 400

		user = UserModel(data['username'], data['password'])
		user.save_to_db()
		_id = user.id

		return _id, 201