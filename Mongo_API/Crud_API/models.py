import bson
from mongoengine import Document, fields

# Create your models here.

class Ship(Document):
    _id  = fields.ObjectIdField(default=bson.ObjectId())
    name = fields.StringField(required=True)




