from app import db


class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    created = db.Column(db.DateTime())
    order_id = db.Column(db.String())
    order_info = db.Column(db.String())