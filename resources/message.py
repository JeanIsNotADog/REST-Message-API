from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.message import MessageModel
from datetime import datetime


class Message(Resource):

	@jwt_required()
	def get(self):
		#
		# parser = reqparse.RequestParser()
		# parser.add_argument('recipient',
		# 					type=int,
		# 					required=True
		# 					)
		# parser.add_argument('start',
		# 					type=int,
		# 					required=True
		# 					)
		# parser.add_argument('limit',
		# 					type=int,
		# 					)
		# data = parser.parse_args()
		user_id = current_identity.id
		# messages = MessageModel.find_by_recipient(data['recipient'])
		messages = MessageModel.find_by_recipient(user_id)
		if messages:
			# res = []
			# for m in messages:
			# 	if m.id >= data['start']:
			# 		res.append(m.json2())
			# if data['limit'] and len(res) > data['limit']:
			# 	return res[0:limit]
			# return res
			return [m.json2() for m in messages]
		return None

	def post(self):
		parser = reqparse.RequestParser()
		parser.add_argument('sender',
							type=int,
							required=True
							)
		parser.add_argument('recipient',
							type=int,
							required=True
							)

		parser.add_argument('content',
							type=str,
							required=True
							)
		data = parser.parse_args()
		message = MessageModel(**data)

		try:
			message.save_to_db()
		except:
			return {'message': 'An error occured when inserting the infomation'}, 500

		return message.json(), 201


