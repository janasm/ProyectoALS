# coding: utf-8
# Listado de críticas de un libro

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
from model.libro import Libro
from webapp2_extras.users import users

class CriticasHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            libro = Libro.recuperaAsg(self.request)
            criticas = Critica.recuperaPorLibro(libro.key)
            valores_plantilla = {
                "libro": libro,
                "criticas": criticas,
                "usr": str(usr.email()),
                "url_usr": users.create_logout_url("/")
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(
                jinja.render_template("criticas.html",
                **valores_plantilla)
            )
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/criticas/listado', CriticasHandler)
], debug=True)