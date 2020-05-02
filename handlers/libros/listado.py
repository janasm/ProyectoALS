import webapp2
from webapp2_extras import jinja2
from model.libro import Libro
from model.critica import Critica
from webapp2_extras.users import users

class LibrosHandler(webapp2.RequestHandler):
    def get(self):
        usr = users.get_current_user()
        if(usr):
            libros = Libro.query().order(-Libro.anho)
            for libro in libros:
                criticas = Critica.recuperaPorLibro(libro.key)
                sumNotasMedia = 0
                for critica in criticas:
                    sumNotasMedia += critica.nota
                if sumNotasMedia != 0 :
                    libro.notaMedia = sumNotasMedia / criticas.count()

            valores_plantilla = {
                "libros": libros,
                "usr": str(usr.email()),
                "url_usr": users.create_logout_url("/")
            }
            jinja = jinja2.get_jinja2(app=self.app)
            self.response.write(
                jinja.render_template("libros.html",
                **valores_plantilla)
            )
        else:
            self.redirect("/")

app = webapp2.WSGIApplication([
    ('/libros/listado', LibrosHandler)
], debug=True)