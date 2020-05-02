
from google.appengine.ext import ndb


class Autor(ndb.Model):
    id = ndb.IntegerProperty(indexed=True)
    nombre = ndb.StringProperty(required=True)