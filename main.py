# -*- coding: utf-8 -*-

import webapp2
import jinja2
import os
import random

template_dir = os.path.join(os.path.dirname(__file__), "templates")
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=False)

class GlavnoMesto(object):
    def __init__(self, mesto, drzava, slika):
        self.mesto = mesto
        self.drzava = drzava
        self.slika = slika

def nekaj_glavnih_mest():
    return [
        GlavnoMesto("Ljubljana", "Slovenia", "Ljubljana.jpg"),
        GlavnoMesto("Rome", "Italy", "Rome.jpg"),
        GlavnoMesto("Paris", "France", "Paris.jpg"),
        GlavnoMesto("Madrid", "Spain", "Madrid.jpg"),
        GlavnoMesto("Zagreb", "Croatia", "Zagreb.jpg"),
        GlavnoMesto("Wien", "Austria", "Wien.jpg"),
        GlavnoMesto("Zürich", "Swiss", "Zurich.jpg"),
        GlavnoMesto("Sarajevo", "Bosnia", "Sarajevo.jpg"),
        GlavnoMesto("Beograd", "Serbia", "Beograd.jpg"),
        GlavnoMesto("Athens", "Greece", "Athens.jpg"),
        GlavnoMesto("Podgorica", "Montenegro", "Podgorica.jpg"),
        GlavnoMesto("Tirana", "Albania", "Tirana.jpg"),
        GlavnoMesto("Skopje", "Macedonia", "Skopje.jpg"),
        GlavnoMesto("London", "United Kingdom", "London.jpg"),
        GlavnoMesto("Berlin", "Germany", "Berlin.jpg"),
    ]

# handlers
class UganiHandler(webapp2.RequestHandler):
    def get(self):
        prestolnica = nekaj_glavnih_mest()[random.randint(0, 14)]

        template = jinja_env.get_template("ugani.html")
        return self.response.write(template.render({"prestolnica": prestolnica}))

class RezultatHandler(webapp2.RequestHandler):
    def post(self):
        odgovor = self.request.get("odgovor")
        mesto = self.request.get("mesto")
        rezultat_ugibanja = odgovor == mesto

        template = jinja_env.get_template("rezultat.html")
        return self.response.write(template.render({
            "mesto": mesto,
            "odgovor": odgovor,
            "rezultat_ugibanja": rezultat_ugibanja
        }))

# URLs
app = webapp2.WSGIApplication([
    webapp2.Route('/', UganiHandler),
    webapp2.Route('/rezultat', RezultatHandler)
], debug=True)
