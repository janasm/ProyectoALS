# coding: utf-8
# Nueva critica

import webapp2
from webapp2_extras import jinja2
from model.critica import Critica
from model.libro import Libro
import time
import datetime
from webapp2_extras.users import users

class NuevaCriticaHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            valores_plantilla = {
                "libro" : Libro.recuperaAsg(self.request),
                "usr": usr,
                "url_usr": users.create_logout_url("/")
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(
                jinja.render_template("nueva_critica.html",
                **valores_plantilla)
            )
        else:
            return self.redirect("/")


    def post(self):
        usr = users.get_current_user()
        if(usr):
            str_nota = self.request.get("nota")
            comentario = self.request.get("comentario")
            fecha = datetime.datetime.now()
            libro = Libro.recuperaAsg(self.request)
            usuario= str(usr.email())

            try:
                nota = int(str_nota)
            except ValueError:
                nota = -1
            if (nota < 0 or not(comentario) or not(libro)) :
                return self.response.write("Error")
            else:
                critica = Critica(libro=libro.key, nota=nota, comentario=comentario, fecha=fecha, usuario=usuario)
                critica.put()
                time.sleep(1)
                return self.redirect("/criticas/listado?asg=" + libro.key.urlsafe())
        else:
            return self.redirect("/")

app = webapp2.WSGIApplication([
    ('/criticas/nueva', NuevaCriticaHandler)
], debug=True)