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
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__)))

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
            npcs.weapon.name == self.request.get('weapon'))
        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == self.request.get('armor'))
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
        # monster = npcs.Monster()
        # monster.name = self.request.get('name')
        # monster.hp = self.request.get('hp')
        # monster.max_hp = self.request.get('max_hp')
        # monster.strength = self.request.get('strength')
        # monster.dexterity = self.request.get('dexterity')
        # monster.intel = self.request.get('intel')
        # monster.weapon = npcs.weapon.query().filer(
        #     npcs.weapon.name == self.request.get('weapon'))
        # monster.armor = npcs.armor.query().filer(
        #     npcs.armor.name == self.request.get('armor'))
        debug_template = jinja_env.get_template('templates/debug_monster.html')
        html = debug_template.render(
        )
        self.response.write(html)

class DebugPlayerHandler(webapp2.RequestHandler):
    def get(self):
        temp_weapon = npcs.weapon.query().filter(
            npcs.weapon.name == self.request.get('weapon'))
        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == self.request.get('armor'))
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
            gold = int(self.request.get('gold')),)
        player.put()
        # player = npcs.player()
        # player.name = self.request.get('name')
        # player.hp = int(self.request.get('hp'))
        # player.max_hp = int(self.request.get('max_hp'))
        # player.strength = int(self.request.get('stength'))
        # player.dexterity = int(self.request.get('dexterity'))
        # player.intel = int(self.request.get('intel'))
        # player.weapon = npcs.weapon.query().filer(
        #     npcs.weapon.name == self.request.get('weapon'))
        # player.armor = npcs.armor.query().filer(
        #     npcs.armor.name == self.request.get('armor'))
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

# This is the variable for the logs.
# It defaults to 5 empty strings in case there are
# less than 5 messages to display on the first round.
# This is outside of the handler to make sure it persists
# between rounds of combat.
messages = ['','','','','']

class GameLoadHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        try:
            player = npcs.player.query().filter(
                npcs.player.name == "Test_Player"
            )
            player = player.get().key

            enemy = npcs.monster.query().filter(
                npcs.monster.name == "Shadow_Link"
            )
            enemy = enemy.get().key

            combat = game_loop.Combat(player, enemy)

            enemy = enemy.get()
            player = player.get()

            if (player.hp > 0 and enemy.hp > 0):
                try:
                    global messages
                    playerChoice = self.request.get('action')
                    combat.combat_loop(playerChoice)
                    if player.was_hit:
                        messages.append("%s hit %s for %s damage" %(enemy.name, player.name, player.hurt))
                    else:
                        messages.append("%s missed %s" %(enemy.name, player.name))
                    if enemy.was_hit:
                        messages.append("%s hit %s for %s damage" %(player.name, enemy.name, enemy.hurt))
                    else:
                        messages.append("%s missed %s" %(player.name, enemy.name))
                    if enemy.hp <= enemy.max_hp/2:
                        messages.append("%s is looking weak" %(enemy.name))
                except(ValueError):
                    placeholder = ("You encountered %s" % enemy.name)
                    messages.append(placeholder)
        # Error handler in case database is missing entities.
        except(AttributeError):
            placeholder = 'ERROR: Models missing from NDB'
            messages.append(placeholder)
        print messages
        messages = messages[-5:]
        print messages
        html = game_template.render({
            'log1':messages[0],
            'log2':messages[1],
            'log3':messages[2],
            'log4':messages[3],
            'log5':messages[4],
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

class MainGame(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render()
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/debug', DebugHandler),
    ('/debug/monster', DebugMonsterHandler),
    ('/debug/player', DebugPlayerHandler),
    ('/debug/armor', DebugArmorHandler),
    ('/debug/weapon', DebugWeaponHandler),
    ('/game', GameHandler),
    # ('/game/debug', GameDebugHandler),
    ('/game/load', GameLoadHandler),
    ('/game/story', GameStoryHandler),
    ('/game/arcade', GameArcadeHandler),
    ("game.html", MainGame),
    ("/maingame", MainGame),
], debug=True)
