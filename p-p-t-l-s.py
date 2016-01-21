#!/usr/bin/env python
#  -*-coding:utf-8-*-
import time
from time import sleep
import random

sus = "-" * 35
tab = " " * 4
depo = ["piedra", "papel", "tijera", "lagarto", "spock"]
while True:
    x = raw_input("Que eliges? Piedra, papel, tijera, lagarto, Spock:\n(Escribe en minusculas)\n(Control + C para salir)\n" + tab)
    if x not in depo:
        print("No hagas trampa!!!")
        continue

    pc = random.choice(depo)
    sleep(0.5)
    print (("Computadora eligio {}.").format(pc))
    if x == pc:
        print '\n Empate.'
    elif x == 'piedra' and pc == 'tijera':
        print "\n Ganaste! Como es habitual… la piedra aplasta las tijeras."
    elif x == 'papel' and pc == 'piedra':
            print "\n Ganaste! Papel cubre a la piedra"
    elif x == 'tijera' and pc == 'papel':
        print "\n Ganaste! Tijeras cortan el papel"
    elif x == 'piedra' and pc == 'lagarto':
        print "\n Ganaste! La piedra aplasta al lagarto"
    elif x == 'lagarto' and pc == 'spock':
        print "\n Ganaste! Lagarto envenena Spock"
    elif x == 'spock' and pc == 'tijera':
        print "\n Ganaste! Spock destroza las tijeras"
    elif x == 'tijera' and pc == 'lagarto':
        print "\n Ganaste! Las tijeras decapitan al lagarto"
    elif x == 'lagarto' and pc == 'papel':
        print "\n Ganaste! El lagarto se come el papel"
    elif x == 'papel' and pc == 'spock':
        print "\n Ganaste! El papel refuta a Spock"
    elif x == 'spock' and pc == 'piedra':
        print "\n Ganaste! Spock vaporiza la piedra"
    else:
        print "\n Perdiste. {} le gana a {} \n{}".format(pc, x, sus)
