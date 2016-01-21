#!/usr/bin/env python
#  -*-coding:utf-8-*-
import time
from time import sleep
import random

pc_puntos = 0
user_puntos = 0
sus = "-" * 35
tab = " " * 4
depo = ["piedra", "papel", "tijera", "lagarto", "spock"]

print """
    Hola! Bienvenido al juego Piedra Papel Tijera Lagarto Spock!\nEstas son las reglas:\n Las tijeras cortan el papel\n El papel cubre a la piedra\n La piedra aplasta al lagarto\n El lagarto envenena a Spock\n Spock destroza las tijeras\n Las tijeras decapitan al lagarto\n El lagarto se come el papel\n El papel refuta a Spock\n Spock vaporiza la piedra\n Y como es habitual... la piedra aplasta las tijeras.\nEl primero en llegar a 10 puntos gana!
"""
sleep(2)
print "\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
sleep(1)
while (pc_puntos < 10 and user_puntos < 10):
    x = raw_input("Que eliges? Piedra, papel, tijera, lagarto o Spock:\n(Control + C para salir)\n(Escribe en minusculas)\n" + tab)
    if x not in depo:
        print("No hagas trampa!!!\nEscribe una de las opciones!!!!\n")
        continue

    pc = random.choice(depo)
    sleep(0.5)
    print (("""Elegiste {}\nComputadora eligio {}\nAsi que:""").format(x, pc))
    if x == pc:
        print '\n Es un Empate...\n'
    elif x == 'piedra' and pc == 'tijera':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Como es habitual... la piedra aplasta las tijeras.\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'papel' and pc == 'piedra':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Papel cubre a la piedra\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'tijera' and pc == 'papel':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Tijeras cortan el papel\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'piedra' and pc == 'lagarto':
        user_puntos = user_puntos + 1
        print "\n Ganaste! La piedra aplasta al lagarto\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'lagarto' and pc == 'spock':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Lagarto envenena Spock\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'spock' and pc == 'tijera':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Spock destroza las tijeras\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'tijera' and pc == 'lagarto':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Las tijeras decapitan al lagarto\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'lagarto' and pc == 'papel':
        user_puntos = user_puntos + 1
        print "\n Ganaste! El lagarto se come el papel\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'papel' and pc == 'spock':
        user_puntos = user_puntos + 1
        print "\n Ganaste! El papel refuta a Spock\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    elif x == 'spock' and pc == 'piedra':
        user_puntos = user_puntos + 1
        print "\n Ganaste! Spock vaporiza la piedra\nGanas un punto!!!\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(user_puntos, pc_puntos)
    else:
        pc_puntos = pc_puntos + 1
        print "\n Lo siento, perdiste: {} le gana a {} \n{}\nPierdes un punto...\nTus puntos son:{}\nY los puntos de la pc son:{}\n".format(pc, x, sus, user_puntos, pc_puntos)
print """
Acabo el juego...
El ganador es...
"""
sleep(2)
if pc_puntos == 10:
    print "La computadora!"
else:
    print "Tu!"
print "Gracias por jugar!"
