# coding: utf-8
# Nueva critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
from model.libro import Libro
import time
import datetime
from google.appengine.ext import ndb

class NuevaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "libro" : Libro.recuperaAsg(self.request)
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("nueva_critica.html",
            **valores_plantilla)
        )

    def post(self):
        str_nota = self.request.get("nota")
        comentario = self.request.get("comentario")
        fecha = datetime.datetime.now()
        libro = Libro.recuperaAsg(self.request)
        usuario= 0

        try:
            nota = int(str_nota)
        except ValueError:
            nota = -1
        if (nota < 0 or not(comentario) or not(libro)) :
            return self.response.write("Error")
        else:
            critica = Critica(libro=libro.key, nota=nota, comentario=comentario, fecha=fecha)
            critica.put()
            time.sleep(1)
            return self.redirect("/criticas/listado?asg=" + libro.key.urlsafe())

app = webapp2.WSGIApplication([
    ('/criticas/nueva', NuevaCriticaHandler)
], debug=True)