#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

# coding: utf-8

import webapp2
from webapp2_extras import jinja2
from model.usuario import Usuario
import time


class MainHandler(webapp2.RequestHandler):
    def get(self):
        valores_plantilla = {
        }
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(
            jinja.render_template("registro.html",
                                  **valores_plantilla)
        )

    def post(self):
        usuario = self.request.get("usuario")
        password = self.request.get("password")

        if((usuario) and (password)):
            try:
                usuario_pre = Usuario.query(Usuario.nombre == usuario and Usuario.password == password).order(Usuario.nombre)
            except ValueError:
                usuario_pre = None

            if (usuario_pre and usuario_pre.count() > 0):
                return self.response.write("Ya existe un usuario con este nombre.")
            else:
                usuario = Usuario(nombre=usuario, password=password)
                usuario.put()
                time.sleep(1)
                return self.redirect("/")
        else:
            return ("Error en el registro.")


app = webapp2.WSGIApplication([
    ('/registro', MainHandler)
], debug=True)
