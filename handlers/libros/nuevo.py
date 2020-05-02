# coding: utf-8
#Nuevo libro

import webapp2
from webapp2_extras import jinja2
from model.libro import Libro

class NuevoLibroHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nuevo_libro.html",
            **valores_plantilla)
        )

    def post(self):
        self.response.write("Creación de libro")

app = webapp2.WSGIApplication([
    ('/libros/nuevo', NuevoLibroHandler)
], debug=True)