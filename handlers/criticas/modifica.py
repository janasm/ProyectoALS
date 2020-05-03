# coding: utf-8
# Modificar critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
import time
from webapp2_extras.users import users

class ModificaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            valores_plantilla = {
                "critica": Critica.recupera(self.request),
                "usr": usr,
                "url_usr": users.create_logout_url("/")
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(
                jinja.render_template("modifica_critica.html",
                **valores_plantilla)
            )
        else:
            return self.redirect("/")

    def post(self):
        usr = users.get_current_user()
        if(usr):
            str_nota = self.request.get("nota")
            comentario = self.request.get("comentario")

            try:
                nota = int(str_nota)
            except ValueError:
                nota = -1
            if nota < 0 :
                return self.response.write("Error")
            else:
                critica = Critica.recupera(self.request)
                critica.nota = nota
                if comentario:
                    critica.comentario = comentario
                critica.put()
                time.sleep(1)
                return self.redirect("/criticas/listado?asg=" + critica.libro.urlsafe())
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/criticas/modifica', ModificaCriticaHandler)
], debug=True)