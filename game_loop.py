# July 23, 2018
# redesigned-computing-machine
# the overly complicated game loop

from google.appengine.ext import ndb

import npcs
import random
import jinja2

# Damage function for combat. Separated for simplicity.
def damage(player1, player2):
    # Player1 is attacker, player2 is defender

    hit = random.randint(1, 20) + int(player1.intel/7.5)
    dodge = random.randint(1, 20) + int(player2.speed/7.5)
    dmg = 0

    # Checks if attack hits based on random chance, and stats.
    if hit >= dodge:
        # Formula for damage.
        dmg = (((player1.strength + player1.weapon.get().power) /
            ((10 - (player1.dexterity / 3))/
            1 + (player2.armor.get().resistance / 100))))
    return int(dmg)

class Combat(object):
    def __init__(self, thing1, thing2):
        # Thing1 and Thing2 are keys for player and enemy objects.
        self.player = thing1.get()
        self.enemy = thing2.get()

    def combat_loop(self, playerChoice):
        # Speed rating decides if either the player or enemy goes first
        if(self.player.speed > self.enemy.speed):
            faster = self.player
            slower = self.enemy

        # In case of speed tie, first turn is chosen randomly each round.
        elif(self.player.speed == self.enemy.speed):
            choice = random.randint(0, 1)
            if(choice == 1):
                faster = self.player
                slower = self.enemy
            else:
                faster = self.enemy
                slower = self.player

        else:
            faster = self.enemy
            slower = self.player

        print (faster.name) ###DEBUG TOOL###

        # The code allows for various options in combat, but
        # Right now the only option is attack.
        if playerChoice == 'attack':
            if faster == self.player:
                dmg = damage(self.player, self.enemy)
                self.enemy.hp -= dmg
                if dmg != 0:
                    # These variables are stored in the database to
                    # be accessed between the various pythons files
                    # without the need for returns. These variables
                    # determine what the log says.
                    self.enemy.was_hit = True
                    self.enemy.hurt = dmg
                else:
                    self.enemy.was_hit = False
                    self.enemy.hurt = dmg
                # Check to ensure opponent isn't dead before they take their turn.
                if self.enemy.hp > 0:
                    dmg = damage(self.enemy, self.player)
                    self.player.hp -= dmg
                    if dmg != 0:
                        self.player.was_hit = True
                        self.player.hurt = dmg

                        self.player.was_hit = True
                        self.player.hurt = dmg
                    else:
                        self.player.was_hit = False
                        self.player.hurt = dmg
            else:
                dmg = damage(self.enemy, self.player)
                self.player.hp -= dmg
                if dmg != 0:
                    self.player.was_hit = True
                    self.player.hurt = dmg
                else:
                    self.player.was_hit = False
                    self.player.playerhurt = dmg
                if self.player.hp > 0:
                    dmg = damage(self.player, self.enemy)
                    self.enemy.hp -= dmg
                    if dmg != 0:
                        self.enemy.was_hit = True
                        self.enemy.hurt = dmg
                    else:
                        self.enemy.was_hit = False
                        self.enemy.hurt = dmg

        print(self.player.hp) ###DEBUG TOOL###
        print(self.enemy.hp) ###DEBUG TOOL###
        
        self.player.put()
        self.enemy.put()
