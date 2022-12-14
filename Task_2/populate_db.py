import json

from app import db
from models.orders import Orders

print('recreating DB tables')
db.drop_all()
db.create_all()

print('adding dummy data')

data = json.loads(open('data.json').read())

for d in data:
    db.session.add(Orders(**d))

db.session.commit()
