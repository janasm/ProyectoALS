# coding: utf-8
# Eliminar critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
import time

class EliminaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        critica = Critica.recupera(self.request)
        libroKey = critica.libro.urlsafe()
        critica.key.delete()
        time.sleep(1)
        return self.redirect("/criticas/listado?asg=" + libroKey)

app = webapp2.WSGIApplication([
    ('/criticas/elimina', EliminaCriticaHandler)
], debug=True)