# July 23, 2018
# redesigned-computing-machine
# An open source game engine for online rpgs using the appEngine platform.

import os
import jinja2
import random
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    get(self):
        pass

app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
