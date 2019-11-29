import bson
from mongoengine import Document, fields

# Create your models here.

class Ship(Document):
    _id  = fields.ObjectIdField(default=bson.ObjectId())
    name = fields.StringField(required=True)
    model = fields.StringField(required=True)
    manufacturer = fields.StringField()
    cost_in_credits = fields.StringField()
    length = fields.StringField()
    max_atmosphering_speed = fields.StringField()
    crew = fields.StringField()
    passengers = fields.StringField()
    cargo_capacity = fields.StringField()
    consumables = fields.StringField()
    hyperdrive_rating = fields.StringField()
    MGLT = fields.StringField()
    starship_class = fields.StringField()
    pilots = fields.ListField(fields.StringField())
    films = fields.ListField(fields.StringField())
    created = fields.StringField()
    edited = fields.StringField()
    url = fields.StringField()
    





