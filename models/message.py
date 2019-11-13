from db import db
from datetime import datetime


class MessageModel(db.Model):
	__tablename__='messages'

	id = db.Column(db.Integer, primary_key=True)
	sender = db.Column(db.Integer)
	recipient = db.Column(db.Integer, db.ForeignKey('users.id'))
	content = db.Column(db.String)

	def __init__(self, sender, recipient, content):
		self.sender = sender
		self.recipient = recipient
		self.content = content

	def json(self):
		now = datetime.now()
		timestamp = datetime.timestamp(now)
		timestamp = datetime.fromtimestamp(timestamp).isoformat()

		return {'id': self.recipient, 'timestamp': timestamp}

	def json2(self):
		return {'id': self.recipient, 'sender': self.sender, 'recipient': self.recipient}

	@classmethod
	def find_by_recipient(cls, recipient_id):
		return cls.query.filter_by(recipient=recipient_id).all()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()


