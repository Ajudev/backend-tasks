from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from views.display import OrderDisplay

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.Config')
db = SQLAlchemy(app)

api.add_resource(OrderDisplay, '/fetch-orders')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)