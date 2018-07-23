# July 23, 2018
# redesigned-computing-machine
# An open source game engine for online rpgs using the appEngine platform.

from google.appengine.ext import ndb

import os
import jinja2
import random
import webapp2

import game-loop

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    get(self):
        main_template = jinja_env.get_template('main.html')
        html = main_template.render(

        )
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
