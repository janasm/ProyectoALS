#Critica perteneciente a un libro y publicada por un usuario

from google.appengine.ext import ndb
from libro import Libro
from usuario import Usuario

class Critica(ndb.Model):
    id = ndb.IntegerProperty(indexed=True)
    libro = ndb.KeyProperty(kind=Libro)
    usuario = ndb.KeyProperty(kind=Usuario)
    nota = ndb.IntegerProperty(required=True)
    comentario = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True)
