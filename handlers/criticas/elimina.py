# coding: utf-8
# Eliminar critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
import time
from webapp2_extras.users import users

class EliminaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        urs = users.get_current_user()
        if(urs):
            critica = Critica.recupera(self.request)
            libroKey = critica.libro.urlsafe()
            critica.key.delete()
            time.sleep(1)
            return self.redirect("/criticas/listado?asg=" + libroKey)
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/criticas/elimina', EliminaCriticaHandler)
], debug=True)