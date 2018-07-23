# July 23, 2018
# redesigned-computing-machine
# the basic game loop

from google.appengine.ext import ndb

import npcs
class Combat(object):
    enemy = random.choice(enemies) #choose from the enemies list
    while(#idk what macks wants here =/):

        if(player.speed > Enemy.speed): #speed rating decides if either the player or enemy goees first
            faster = player
            slower = enemy
        else:
            faster = enemy
            slower = player

        if faster = player:
            #how would we do this part? how do we declare that this person goes first?
    playerChoice = jinja.FileSystemLoader(#where ever its at)
    print("Select an option!")

    if player.Choice = fight:
        #chance to hit
        if hit = True:
            print("You have hit" + " " + enemy)
            #how can we determine how much damage was done?
            enemy.hp = hp - dmg
        else:
            print("You have missed")
            if enemy.hp <= '0':
                print("Dead")
            else:
                enemy.Attack()
                #chance to hit
                if hit = True:
                    print("The" + enemy + "has hit you")
                    #how to determine damage
                    player.hp = hp - dmg
                else:
                    print("Enemy has missed")
                    if player.hp <= '0':
                        print("GAME OVER")



    elif player.Choice = run:
        quit.Combat
        #takes me back to where i was before the combat began
    elif player.Choice = item:
        print("Select an item!")
        #actually select the item

    else:
        #save the game
