from flask_restful import Resource
import sqlite3

class Check(Resource):
    def post(self):
        connection = sqlite3.connect("challenge.db")
        cursor = connection.cursor()

        query = "SELECT 1"
        (res, ) = cursor.execute(query).fetchone()
        if res != 1:
            raise Exception("unexpected query result")
        return {'health': "ok"}, 200

