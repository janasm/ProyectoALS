# coding: utf-8
# Modificar critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
import time

class ModificaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
            "critica": Critica.recupera(self.request)
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("modifica_critica.html",
            **valores_plantilla)
        )

    def post(self):
        str_nota = self.request.get("nota")
        comentario = self.request.get("comentario")

        try:
            nota = int(str_nota)
        except ValueError:
            nota = -1
        if (nota < 0 or not(comentario)) :
            return self.response.write("Error")
        else:
            critica = Critica.recupera(self.request)
            critica.nota = nota
            if comentario:
                critica.comentario = comentario
            critica.put()
            time.sleep(1)
            return self.redirect("/criticas/listado?asg=" + critica.libro.urlsafe())

app = webapp2.WSGIApplication([
    ('/criticas/modifica', ModificaCriticaHandler)
], debug=True)