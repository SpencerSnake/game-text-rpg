# July 23, 2018
# redesigned-computing-machine
# npcs database. Storing player and enemies.

from google.appengine.ext import ndb

# This is the base npc class containing all
# the statistics required for combat. It's
# used by both players and enemies.
class npc(ndb.Model):
    # name displayed to the webpage
    name = ndb.StringProperty(required=True)
    # hp remaining
    hp = ndb.IntegerProperty(required=True)
    # determines turn order
    speed = ndb.IntegerProperty(require=True)
    # determines chance to hit
    armor = ndb.IntegerProperty(require=True)
    # determines damage
    strength = ndb.IntegerProperty(required=True)

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
    pass ### add variables in phase 2
