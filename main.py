# July 23, 2018
# redesigned-computing-machine
# An open source game engine for online rpgs using the appEngine platform.

from google.appengine.ext import ndb

import os
import jinja2
import random
import webapp2

#import game-loop

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('templates/main.html')
        html = main_template.render(

        )
        self.response.write(html)

class DebugHandler(webapp2.RequestHandler):
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugMonsterHandler(webapp2.RequestHandler):
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugPlayerHandler(webapp2.RequestHandler):
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugArmorHandler(webapp2.RequestHandler):
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugWeaponHandler(webapp2.RequestHandler):
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(

        )
        self.response.write(html)

class GameHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render(

        )
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/debug', DebugHandler),
    ('/debug/monster', DebugMonsterHandler),
    ('/debug/player', DebugPlayerHandler),
    ('/debug/armor', DebugArmorHandler),
    ('/debug/weapon', DebugWeaponHandler),
    ('/game', GameHandler)
], debug=True)
