from datetime import datetime
from app import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime(), default=datetime.now())
    order_id = db.Column(db.String(50))
    order_info = db.Column(db.String(50))