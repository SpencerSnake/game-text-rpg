# July 23, 2018
# redesigned-computing-machine
# the basic game loop

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

    def combat_loop(self):
        self.player.hp = self.player.max_hp
        self.enemy.hp = self.enemy.max_hp
        while(self.player.hp > 0 and self.enemy.hp > 0):
            playerChoice = 'fight' #jinja.FileSystemLoader(/noWhereYet)
            if(self.player.speed > self.enemy.speed): #speed rating decides if either the player or enemy goees first
                faster = self.player
                slower = self.enemy
            else:
                faster = self.enemy
                slower = self.player

            print (faster)

            if playerChoice == 'fight':
                if faster == self.player:
                    dmg = damage(self.player, self.enemy)
                    self.enemy.hp -= dmg
                    if self.enemy.hp > 0:
                        dmg = damage(self.enemy, self.player)
                        self.player.hp -= dmg
                else:
                    dmg = damage(self.enemy, self.player)
                    self.player.hp -= dmg
                    if self.player.hp > 0:
                        dmg = damage(self.player, self.enemy)
                        self.enemy.hp -= dmg

            print(self.player.hp)
            print(self.enemy.hp)
        if self.enemy.hp <= 0:
            return("Enemy is Dead")
        elif self.player.hp <= 0:
            return("GAME OVER")
#call to datastore
