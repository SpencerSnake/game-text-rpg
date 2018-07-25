# July 23, 2018
# redesigned-computing-machine
# An open source game engine for online rpgs using the appEngine platform.

from google.appengine.ext import ndb

import npcs
import game_loop

import os
import jinja2
import random
import webapp2

jinja_env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

player = npcs.player.query().filter(
    npcs.player.name == "Test_Player"
)
player = player.get().key

enemy = npcs.monster.query().filter(
    npcs.monster.name == "Shadow_Link"
)
enemy = enemy.get().key

combat = game_loop.Combat(player, enemy)

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

        temp_weapon = npcs.weapon.query().filter(
            npcs.weapon.name == "Test_Weapon")

        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == "Test_Armor")
        monster = npcs.monster(
            name = self.request.get('name'),
            hp = int(self.request.get('hp')),
            max_hp = int(self.request.get('max_hp')),
            strength = int(self.request.get('strength')),
            dexterity = int(self.request.get('dexterity')),
            intel = int(self.request.get('intel')),
            weapon = temp_weapon.fetch(1)[0].key,
            armor = temp_armor.fetch(1)[0].key,
            speed = int((int(self.request.get('strength')*10)/
                (temp_armor.get().weight+temp_weapon.get().weight)+
                (int(self.request.get('dexterity'))*1.2)))
        )
        monster.put()
        debug_template = jinja_env.get_template('templates/debug_monster.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugPlayerHandler(webapp2.RequestHandler):
    def get(self):

        temp_weapon = npcs.weapon.query().filter(
            npcs.weapon.name == "Test_Weapon")

        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == "Test_Armor")
        player = npcs.player(
            name = self.request.get('name'),
            hp = int(self.request.get('hp')),
            max_hp = int(self.request.get('max_hp')),
            strength = int(self.request.get('strength')),
            dexterity = int(self.request.get('dexterity')),
            intel = int(self.request.get('intel')),
            weapon = temp_weapon.fetch(1)[0].key,
            armor = temp_armor.fetch(1)[0].key,
            speed = int((int(self.request.get('strength')*10)/
                (temp_armor.get().weight+temp_weapon.get().weight)+
                (int(self.request.get('dexterity'))*1.2))),
            xp = int(self.request.get('xp')),
            gold = int(self.request.get('gold')),
        )
        player.put()
        debug_template = jinja_env.get_template('templates/debug_player.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugArmorHandler(webapp2.RequestHandler):
    def get(self):
        armor = npcs.armor(
            name = self.request.get('name'),
            resistance = int(self.request.get('resistance')),
            weight = int(self.request.get('weight')),
        )
        armor.put()
        debug_template = jinja_env.get_template('templates/debug_armor.html')
        html = debug_template.render(

        )
        self.response.write(html)

class DebugWeaponHandler(webapp2.RequestHandler):
    def get(self):
        weapon = npcs.weapon(
            name = self.request.get('name'),
            power = int(self.request.get('power')),
            weight = int(self.request.get('weight')),
        )
        weapon.put()
        debug_template = jinja_env.get_template('templates/debug_weapon.html')
        html = debug_template.render(

        )
        self.response.write(html)

class GameHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render(

        )
        self.response.write(html)

class GameLoadHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        result = combat.combat_loop()
        html = game_template.render({
            "result":result
        })
        self.response.write(html)

class GameStoryHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render(

        )
        self.response.write(html)

class GameArcadeHandler(webapp2.RequestHandler):
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
    ('/game', GameHandler),
    ('/game/load', GameLoadHandler),
    ('/game/story', GameStoryHandler),
    ('/game/arcade', GameArcadeHandler),
], debug=True)
