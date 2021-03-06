# coding: utf-8
#Nuevo libro

import webapp2
from webapp2_extras import jinja2
from model.libro import Libro
import time
from webapp2_extras.users import users

class NuevoLibroHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            valores_plantilla = {
                "usr": usr,
                "url_usr": users.create_logout_url("/")
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(
                jinja.render_template("nuevo_libro.html",
                **valores_plantilla)
            )
        else:
            return self.redirect("/")

    def post(self):
        usr = users.get_current_user()
        if(usr):
            titulo = self.request.get("titulo")
            autor = self.request.get("autor")
            str_anho = self.request.get("anho")
            enlace = self.request.get("enlace")
            try:
                anho = int(str_anho)
            except ValueError:
                anho = -1
            if (anho < 0 or not(titulo) or not (autor) or not (enlace)) :
                return self.response.write("Error")
            else:
                libro = Libro(titulo=titulo, autor=autor, anho=anho, enlace=enlace)
                libro.put()
                time.sleep(1)
                return self.redirect("/libros/listado")
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/libros/nuevo', NuevoLibroHandler)
], debug=True)