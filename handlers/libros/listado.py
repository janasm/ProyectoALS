import webapp2
from webapp2_extras import jinja2
from model.libro import Libro

class LibrosHandler(webapp2.RequestHandler):
    def get(self):
        libros = Libro.query().order(-Libro.anho)
        valores_plantilla = {
            "libros": libros
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("libros.html",
            **valores_plantilla)
        )

app = webapp2.WSGIApplication([
    ('/libros/listado', LibrosHandler)
], debug=True)