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

        if hit >= dodge:
            dmg = (((player1.strength + player1.weapon) / (10 - (player1.dex / 3)))/ 1 + (player2.armor / 100))#i dnt knw how to brk it dwn
        else:
            print("You missed")
    def combat_loop(self):
        while(player.hp > '0' #wait wut):



                #player goes first
                #how would we do this part? how do we declare that this person goes first?
        playerChoice = jinja.FileSystemLoader(#where ever its at):

                if(player.speed > Enemy.speed): #speed rating decides if either the player or enemy goees first
                    faster = player
                    slower = enemy
                else:
                    faster = enemy
                    slower = player

                    if faster == player:
                        damage(player, enemy)
                        if enemy hp > 0:
                            damage(enemy, player)
                    else:
                        damage(enemy, player)
                        if player hp > 0:
                            damage(player, enemy)

            print("Select an option!")

            if player.Choice = fight:
                if hit >= dodge:
                    dmg
                    if hit = True:
                        print("You have hit " + enemy)
                    #how can we determine how much damage was done?
                        enemy.hp = hp - dmg
                    else:
                        print("You have missed")
                        if enemy.hp <= '0':
                            print("Dead")
                        else:
                            enemy.Hit()
                        #chance to hit
                        if hit = True:
                            print("The " + enemy + " has hit you")
                            #how to determine damage
                            player.hp = hp - dmg
                        else:
                            print("Enemy has missed")
                            if player.hp <= '0':
                                print("GAME OVER")]]
