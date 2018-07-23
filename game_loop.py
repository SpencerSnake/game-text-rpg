# July 23, 2018
# redesigned-computing-machine
# the basic game loop

from google.appengine.ext import ndb

import npcs
import random

class Combat(object):
    def __init__(self, thing1, thing2):#it does matter but it doesn't
        player = thing1
        enemy = thing2

    def damage(self, player1, player2):
        hit = random.randInt(1,20) + int(player1.intel/7.5)
        dodge = random.randInt(1,20) + int(player2.speed/7.5) #player 2 is the one BEING hit
        dmg = 0

        if hit >= dodge:
            dmg = (((player1.strength + player1.weapon) / (10 - (player1.dex / 3)))/ 1 + (player2.armor / 100))#i dnt knw how to brk it dwn
        return int(dmg)

        else:
            print("You missed")
    def combat_loop(self):
        while(player.hp > '0' #wait wut):




                #player goes first
                #how would we do this part? how do we declare that this person goes first?
            playerChoice = jinja.FileSystemLoader(/noWhereYet):
                if(player.speed > Enemy.speed): #speed rating decides if either the player or enemy goees first
                    faster = player
                    slower = enemy
                else:
                    faster = enemy
                    slower = player



            print("Select an option!")

            if player.Choice = fight:
                if faster == player:
                    dmg = damage(player, enemy)
                    enemy.hp -= dmg
                    if enemy.hp > 0:
                        dmg = damage(enemy, player)
                        player.hp -= dmg
                else:
                    dmg = damage(enemy, player)
                    player.hp -= dmg
                    if player hp > 0:
                        dmg = damage(player, enemy)
                        enemy.hp -= dmg
                    else:
                        print("You have missed")
                    if enemy.hp <= 0:
                        print("Enemy is Dead")
                    elif player.hp <= 0:
                        print("GAME OVER")
