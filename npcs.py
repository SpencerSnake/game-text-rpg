# July 23, 2018
# redesigned-computing-machine
# npcs database. Storing player and enemies.

from google.appengine.ext import ndb

import webapp2

# This is the base npc class containing all
# the statistics required for combat. It's
# used by both players and enemies.
class npc(ndb.Model):
    # name displayed to the webpage
    name = ndb.StringProperty(required=True)
    # hp remaining
    hp = ndb.IntegerProperty(required=True)
    # maximum hp
    max_hp = ndb.IntegerProperty(required=True)
    # determines turn order, and dodge chance
    speed = ndb.IntegerProperty(required=True)
    # Equipment - determines damage reduction, out of 100
    armor = ndb.KeyProperty(required=True)
    # Equipment - determines base damage
    weapon = ndb.KeyProperty(required=True)
    # determines base damage
    strength = ndb.IntegerProperty(required=True)
    # determines damage calculation
    dexterity = ndb.IntegerProperty(required=True)
    # determines chance to hit
    intel = ndb.IntegerProperty(required=True)
    # determines message in the combat log
    was_hit = ndb.BooleanProperty(required=False)
    # how much damage it took
    hurt = ndb.IntegerProperty(required=False)




# This is the weapon class. It is used by all npcs
# to determine damage values. Certain monsters, and
# all players can use several different weapons.
class weapon(ndb.Model):
    # name displayed on the webpage
    name = ndb.StringProperty(required=True)
    # determines base damage
    power = ndb.IntegerProperty(required=True)
    # determines speed of wielder
    weight = ndb.IntegerProperty(required=True)



# This is the armor class. It is used by all npcs
# to determine damage reduction. Certain monsters,
# and all players can use several different types
# of armor.
class armor(ndb.Model):
    # name displayed on webpage
    name = ndb.StringProperty(required=True)
    # determines damage reduction, out of 100
    resistance = ndb.IntegerProperty(required=True)
    # determines speed of wielder
    weight = ndb.IntegerProperty(required=True)



# This is the player class, used by all users
# of the game. It contains variables used
# exclusively in the player encounters.
class player(npc):
    # gold acquired
    gold = ndb.IntegerProperty(required=True)
    # experience points acquired
    xp = ndb.IntegerProperty(required=True)
    # player inventory. Stored as string list
    # and parsed.
    inventory = ndb.StringProperty(repeated=True)



# This is the monster class, used by all
# all enemies in the game. It contains data
# used behind the scenes to determine various
# results.
class monster(npc):
    pass ### add data in phase 2
