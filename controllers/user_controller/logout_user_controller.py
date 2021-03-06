from flask_restful import Resource
from flask import session


class LogoutUserController(Resource):
    def get(self):
        session.permanent = True
        session.pop("user_id")
        return "200"

    def post(self):
        return "USE GET: api/v1/users/logout"
