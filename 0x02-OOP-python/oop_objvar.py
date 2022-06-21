#!/usr/bin/python3
"""demo of class and object
    variables
"""
class Robot:
    """Represent a robot, with a name."""
    population = 0
    # class var, tells robots count

    def __init__(self, name):
        """Constructor to initialize data for a new Robot."""
        self.name = name
        # tell us when a new robot is created
        print("(Initializing {}...)".format(self.name))
        # increase robots population when a new one is created
        Robot.population += 1

    def die(self):
        """I am dying"""
        print("{} no master, please NO!".format(self.name))
        print("{} is now offline.\n".format(self.name))
        # Robots population drops because this one died
        Robot.population -= 1

        if Robot.population == 0:
            print("{} was the last bot standing, that was a close call.\n".format(self.name))
        else:
            print("We still have {:d} active robots.\n".format(Robot.population))

    def say_hi(self):
        """Yes, Robots can greet too lol"""
        print("Greatings Master, call me {}.".format(self.name))

    @classmethod
    def how_many(cls):
        """Tells the current robots population."""
        print("We have {:d} active bots.\n".format(cls.population))

bot1 = Robot('R2-D2')
bot1.say_hi()
Robot.how_many()

bot2 = Robot('C-3PO')
bot2.say_hi()
Robot.how_many()

print("\nOh no! the BotsOS has been hacked, we need to act fast! Initaite shutdown protocol.\n")

bot1.die()
bot2.die()

Robot.how_many()
