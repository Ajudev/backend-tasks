from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
import redis

from views.display import OrderDisplay

app = Flask(__name__)
api = Api(app)
app.config.from_object('config.Config')
db = SQLAlchemy(app)
redis_client = redis.Redis(host="redis_cache", port=6379, db=0)

api.add_resource(OrderDisplay, '/fetch-orders', '/fetch-orders/<int:page>')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)