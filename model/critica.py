#Critica perteneciente a un libro y publicada por un usuario

from google.appengine.ext import ndb
from libro import Libro
from usuario import Usuario

class Critica(ndb.Model):
    libro = ndb.KeyProperty(kind=Libro)
    usuario = ndb.StringProperty(required=True)
    nota = ndb.IntegerProperty(required=True)
    comentario = ndb.StringProperty(required=True)
    fecha = ndb.DateTimeProperty(auto_now_add=True)
    alias = ndb.StringProperty()

    @staticmethod
    def recupera(request):
        try:
            id = request.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def recuperaPorLibroYUsuario(libroId, usr):
        return Critica.query(libroId == Critica.libro and usr == Critica.usuario).order(-Critica.fecha)

    @staticmethod
    def recuperaPorLibro(libroId):
        return Critica.query(libroId == Critica.libro).order(-Critica.fecha)