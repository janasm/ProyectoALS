
from google.appengine.ext import ndb


class Usuario(ndb.Model):
    nombre = ndb.StringProperty(required=True)
    password = ndb.StringProperty(required=True)

    @staticmethod
    def recupera(request):
        try:
            id = request.GET["id"]
        except KeyError:
            id = ""

        return ndb.Key(urlsafe=id).get()