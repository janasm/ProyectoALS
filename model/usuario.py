
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    id = ndb.IntegerProperty(indexed=True)
    nombre = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)