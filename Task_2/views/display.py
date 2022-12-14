from flask_restful import Resource
from flask import make_response
from views.helpers import fetch_results



class OrderDisplay(Resource):

    def get(self, page=1):
        """ Simple endpoint that returns orders stored in db """

        try:
            statement = f"select * from orders"

            data = fetch_results(statement, page)

            return make_response(data, 200)

        except Exception as e:
            return make_response({"error": "Internal server error", "message": e.args[0]}, 500)