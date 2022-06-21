#!/usr/bin/python3
from oop_fight import *
def main():
    dagunro = Warrior("Dagunro", 10, 10, 10)
    fadeyi = Warrior("Fadeyi Oloro", 10, 10, 10)

    battle = Battle()

    battle.playRound(dagunro,fadeyi)

main()
