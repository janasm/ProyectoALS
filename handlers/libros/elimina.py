# coding: utf-8
#Eliminar libro

import webapp2
from webapp2_extras import jinja2
from model.libro import Libro
import time
from webapp2_extras.users import users

class EliminaLibroHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            libro = Libro.recuperaId(self.request)
            libro.key.delete()
            time.sleep(1)
            return self.redirect("/libros/listado")
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/libros/elimina', EliminaLibroHandler)
], debug=True)