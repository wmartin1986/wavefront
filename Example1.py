#!/usr/bin/python
import os
from random import randint


class Player:
    name = ""
    defend = False

    def __init__(self, hp, atk):
        self.hp, self.atk = hp, atk
        status = []

    def takeDamage(self, damage):
        if (self.defend == True):
            damage = damage / 3
            self.hp -= damage
        else: self.hp -= damage

    def setName(self, name):
        self.name = name

    def basicAttack(self):
        damage = self.atk + randint(0, 3)
        return damage


#class Warrior(Player):
    #determines special attack


class Monster:
    def __init__(self, hp, atk):
        self.hp, self.atk = hp, atk
        status = []

    def takeDamage(self, damage):
        self.hp -= damage


class Battle:
    characters = []
    monsters = []
    turnOrder = []

    turn = 0
    round = 0
    run = False

    def setupBattle(self, characters, monsters):
        """accepts list of monsters and characters"""
        self.characters.extend(characters)
        self.monsters.extend(monsters)
        # turn order
        '''TODO: Make smarter'''
        self.turnOrder.extend(characters)
        self.turnOrder.extend(monsters)

    def stillFighting(self, fighters):
        for fighter in fighters:
            if fighter.hp > 0:
                return True
        return False

    def win(self, run):
        if self.stillFighting(self.characters) == False:
            return "You died. Try again."
        if self.stillFighting(self.monsters) == False:
            return "You won!"
        if run == True:
            return "You ran!"

    def startBattle(self):
        run = False
        while (self.stillFighting(self.characters) and self.stillFighting(self.monsters)):
            os.system('cls')
            print("You are fighting a minotaur! \n It has %s hp left! \n" % (minotaur.hp))
            if isinstance(self.turnOrder[self.turn], Player):
                '''players turn'''
                thePlayer.defend = False
                print("It's your move. What will you do?")
                option = input("(A)ttack (D)efend (R)un: ")
                if (option == "a"):
                    print("You strike with all your might! \n")
                    damage = thePlayer.basicAttack()
                    print("You deal %s damage to the minotaur! \n" % (damage))
                    minotaur.takeDamage(damage)
                    self.turn+= 1
                elif (option == "d"):
                    print("You defend!")
                    while (isinstance(self.turnOrder[self.turn], thePlayer) == False):
                        thePlayer.defend = True
                    self.turn += 1
                elif (option == "r"):
                    run = True
                    break

                else:
                    input("I didn't understand that. Press Enter")

                print("The Minotaur swings his fist and lands a blow.")
                mobdamage = minotaur.atk + randint(0, 1)
                thePlayer.takeDamage(mobdamage)
                if (thePlayer.hp > 0):
                    print("Your HP is %s" % (thePlayer.hp))
                if (thePlayer.hp <= 0):
                    print("You have taken a fatal blow")
                self.turn += 1
            if self.turn >= len(self.turnOrder):
                self.turn = 0
        self.win(run)


hp = 0
while hp >= 10 or hp <= 1:
    hp = int(input("Divide 10 points between HP and Attack -- What is HP?"))
atk = 10 - hp
hp = hp * 3
thePlayer = Player(hp, atk)

charName = input("Give your character a name.\n")
thePlayer.setName(charName)

print("Welcome to our story, " + thePlayer.name + ".\n")
print("Your stats are set to %s HP, %s Attack Power." % (thePlayer.hp, thePlayer.atk))

input("Let's begin! \nPress Enter")
minotaur = Monster(10, 3)
input("Oh no a Minotaur attacks! \nPress Enter")

battle = Battle()
battle.setupBattle([thePlayer], [minotaur])
battle.startBattle()
