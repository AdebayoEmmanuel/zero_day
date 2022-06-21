#!/usr/bin/python3
import random
import math
class Warrior:
    """A warrior has a default name of Abija
       and is weak AF unless otherwise stated
    """

    def __init__(self, name="Abija", health=0, maxAttack=0, maxBlock=0):
        self.name = name
        self.health = health
        self.maxAttack = maxAttack
        self.maxBlock = maxBlock
    
    def offense(self):
        """A warrior can attack with random
           value from 0.5 to 1.5 times maxAttack
        """
        attack = self.maxAttack * (random.random() + .5)
        
        return attack

    def defense(self):
        """A warrior can block an attack
           otherwise wont be fair
        """
        block = self.maxBlock * (random.random() + .5)
        
        return block

class Battle:
    """Every round played has an attack and a defense that 
       produces an outcome as defined in the battle class
    """
    @staticmethod
    def getOutcome(warriorA, warriorB):
        attack = warriorA.offense()
        defense = warriorB.defense()

        damage_dealt = math.ceil(defense - attack)

        warriorB.health = warriorB.health - damage_dealt

        print("{} attacked {} and dealt {} damage".format(warriorA.name, warriorB.name, damage_dealt))
        print("{} is down to {} HP".format(warriorB.name, warriorB.health))

        if warriorB.health <= 0:
            print("{} is dead. {} Wins!".format(warriorB.name, warriorA.name))
            return "Game Over"
        else:
            return "Fight on"

    def playRound(self, warrior1, warrior2):
        while True:
            if self.getOutcome(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
            if self.getOutcome(warrior2, warrior1) == "Game Over":
                print("Game over")
                break
