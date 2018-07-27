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
    # Loads the main page
    def get(self):
        main_template = jinja_env.get_template('templates/main.html')
        html = main_template.render(
        )
        self.response.write(html)

class DebugHandler(webapp2.RequestHandler):
    # Loads the debug menu, allowing you to create new objects for the database.
    def get(self):
        debug_template = jinja_env.get_template('templates/debug.html')
        html = debug_template.render(
        )
        self.response.write(html)

class DebugMonsterHandler(webapp2.RequestHandler):
    # Loads new monster entity into database.
    def get(self):
        temp_weapon = npcs.weapon.query().filter(
            npcs.weapon.name == self.request.get('weapon'))
        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == self.request.get('armor'))
        monster = npcs.monster(
            name=self.request.get('name'),
            hp=int(self.request.get('hp')),
            max_hp=int(self.request.get('max_hp')),
            strength=int(self.request.get('strength')),
            dexterity=int(self.request.get('dexterity')),
            intel=int(self.request.get('intel')),
            weapon=temp_weapon.fetch(1)[0].key,
            armor=temp_armor.fetch(1)[0].key,
            speed=calculate_speed(
                int(self.request.get('strength')),
                temp_armor.get(),
                temp_weapon.get(),
                int(self.request.get('dexterity'))
                ),
        )
        monster.put()
        debug_template = jinja_env.get_template('templates/debug_monster.html')
        html = debug_template.render(
        )
        self.response.write(html)

class DebugPlayerHandler(webapp2.RequestHandler):
    # # Loads new player entity into database.
    def get(self):
        temp_weapon = npcs.weapon.query().filter(
            npcs.weapon.name == self.request.get('weapon'))
        temp_armor = npcs.armor.query().filter(
            npcs.armor.name == self.request.get('armor'))
        player = npcs.player(
            name=self.request.get('name'),
            hp=int(self.request.get('hp')),
            max_hp=int(self.request.get('max_hp')),
            strength=int(self.request.get('strength')),
            dexterity=int(self.request.get('dexterity')),
            intel=int(self.request.get('intel')),
            weapon=temp_weapon.fetch(1)[0].key,
            armor=temp_armor.fetch(1)[0].key,
            speed=calculate_speed(
                int(self.request.get('strength')),
                temp_armor.get(),
                temp_weapon.get(),
                int(self.request.get('dexterity'))
                ),
            xp=int(self.request.get('xp')),
            gold=int(self.request.get('gold')),
        )
        player.put()
        debug_template = jinja_env.get_template('templates/debug_player.html')
        html = debug_template.render(
        )
        self.response.write(html)

class DebugArmorHandler(webapp2.RequestHandler):
    # Loads new armor entity into database.
    def get(self):
        armor = npcs.armor(
            name=self.request.get('name'),
            resistance=int(self.request.get('resistance')),
            weight=int(self.request.get('weight')),
        )
        armor.put()
        debug_template = jinja_env.get_template('templates/debug_armor.html')
        html = debug_template.render(
        )
        self.response.write(html)

class DebugWeaponHandler(webapp2.RequestHandler):
    # Loads new weapon entity into database.
    def get(self):
        print self.request
        print self.request.get('name')
        weapon = npcs.weapon(
            name=self.request.get('name'),
            power=int(self.request.get('power')),
            weight=int(self.request.get('weight')),
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
        running = True
        try:
            player = npcs.player.query().filter()
            player = player.get().key

            enemy = npcs.monster.query().filter()
            enemy = enemy.get().key

            combat = game_loop.Combat(player, enemy)

            enemy = enemy.get()
            player = player.get()

            print player.hp ###DEBUG TOOL###
            print enemy.hp ###DEBUG TOOL###

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
            # Go to result when player wins or loses.
            else:
                # Loads different page in this case
                game_template = jinja_env.get_template('templates/results.html')
                # Checks whether player won or lost.
                if player.hp < 0:
                    result = "You Lose!"
                else:
                    result = "You Win!"
                # Tells code not to run the other page template
                running = False
                # Resets the statistics of the player and opponent.
                player.hp = player.max_hp
                enemy.hp = enemy.max_hp
                player.was_hit = None
                enemy.was_hit = None
                # Arbitrary numbers increase, prompting you to keep playing the game.
                player.xp += 150
                player.gold += 30
                player.put()
                enemy.put()
                # Resets message log
                messages = ['','','','','']
                html = game_template.render({
                    'result':result
                })
                self.response.write(html)

        # Error handler in case database is missing entities.
        except(AttributeError):
            placeholder = 'ERROR: Models missing from NDB'
            messages.append(placeholder)

        print messages ###DEBUG TOOL###
        # Slices messages back down to the 5 most recent entries.
        messages = messages[-5:]
        print messages ###DEBUG TOOL###
        if running:
            html = game_template.render({
                'log1':messages[0],
                'log2':messages[1],
                'log3':messages[2],
                'log4':messages[3],
                'log5':messages[4],
                'name':player.name,
                'hp':player.hp,
                'max_hp':player.max_hp,
                'xp':player.xp,
                'wp':player.weapon.get().name,
                'gp':player.gold,
            })
            self.response.write(html)

# NOT CURRENTLY USED
class GameStoryHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render(
        )
        self.response.write(html)
# NOT CURRENTLY USED
class GameArcadeHandler(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render(
        )
        self.response.write(html)
# NOT CURRENTLY USED
class MainGame(webapp2.RequestHandler):
    def get(self):
        game_template = jinja_env.get_template('templates/game.html')
        html = game_template.render()
        self.response.write(html)

def calculate_speed(strength, armor, weapon, dexterity):
    print('Called with', strength, dexterity, armor, weapon) ### DEBUG TOOL ###
    # Calculates speed based on several parameters.
    return int(((strength * 3) / (armor.weight + weapon.weight)) + (dexterity * 1.2))

app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/debug', DebugHandler),
    ('/debug/monster', DebugMonsterHandler),
    ('/debug/player', DebugPlayerHandler),
    ('/debug/armor', DebugArmorHandler),
    ('/debug/weapon', DebugWeaponHandler),
    ('/game', GameHandler),
    ('/game/story', GameStoryHandler),
    ('/game/arcade', GameArcadeHandler),
    ('/maingame', GameLoadHandler),
], debug=True)
