# coding: utf-8
#Libro perteneciente a un autor

from google.appengine.ext import ndb
from autor import Autor

class Libro(ndb.Model):
    autor = ndb.StringProperty(required=True)
    titulo = ndb.StringProperty(required=True)
    anho = ndb.IntegerProperty(required=True)
    enlace = ndb.StringProperty(required=True)
    notaMedia = ndb.FloatProperty()

    @staticmethod
    def recuperaId(request):
        try:
            id = request.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()

    @staticmethod
    def recuperaAsg(request):
        try:
            id = request.GET["asg"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()
