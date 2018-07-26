# July 23, 2018
# redesigned-computing-machine
# the overly complicated game loop

from google.appengine.ext import ndb

import npcs
import random
import jinja2

def damage(player1, player2):
    hit = random.randint(1,20) + int(player1.intel/7.5)
    dodge = random.randint(1,20) + int(player2.speed/7.5) #player 2 is the one BEING hit
    dmg = 0

    if hit >= dodge:
        dmg = (((player1.strength + player1.weapon.get().power) /
            ((10 - (player1.dexterity / 3))/
            1 + (player2.armor.get().resistance / 100))))
    return int(dmg)

class Combat(object):
    def __init__(self, thing1, thing2):#it does matter but it doesn't
        self.player = thing1.get()               #it really does
        self.enemy = thing2.get()
        self.messages = []

    def combat_loop(self, playerChoice):
        # Speed rating decides if either the player or enemy goes first
        if(self.player.speed > self.enemy.speed):
            faster = self.player
            slower = self.enemy

        # In case of speed tie, first turn is chosen randomly each round.
        elif(self.player.speed == self.enemy.speed):
            choice = random.randint(0,1)
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

        if playerChoice == 'attack':
            if faster == self.player:
                dmg = damage(self.player, self.enemy)
                self.enemy.hp -= dmg
                if dmg != 0:
                    self.enemy.was_hit = True
                    self.enemy.hurt = dmg
                else:
                    self.enemy.was_hit = False
                    self.enemy.hurt = dmg
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
#call to datastore
