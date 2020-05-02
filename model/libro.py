# coding: utf-8
#Libro perteneciente a un autor

from google.appengine.ext import ndb
from autor import Autor

class Libro(ndb.Model):
    id = ndb.IntegerProperty(indexed=True)
    autor = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)
    anho = ndb.IntegerProperty(required=True)
    enlace = ndb.StringProperty(required=True)
