#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
import time
from nxt.motor import *
import sys
import tty
import termios

metodo = nxt.locator.Method(bluetooth=True)
print"procurando robo..."
b = nxt.locator.find_one_brick(host="00:16:53:1A:68:D8", method=metodo)
print"robo localizado"
motor_esquerdo = Motor(b, PORT_C)
motor_direito = Motor(b, PORT_B)

# FORWARD
def frente():
	motor_esquerdo.run(100)
	motor_direito.run(100)

# BACKWARD
def tras():
	motor_esquerdo.run(-100)
	motor_direito.run(-100)

# STOP
def para():
	motor_direito.idle()
	motor_esquerdo.idle()

# RIGHT
def direito():
	motor_direito.run (-100)
	motor_esquerdo.run(100)

# LEFT
def esquerdo():
	motor_direito.run (100)
	motor_esquerdo.run (-100)

def quit():
	old[3] = old[3] | termios.ECHO
	termios.tcsetattr(fd, termios.TCSADRAIN, old)
	sys.exit()
def distancia():
	print 'Ultrasonic:', Ultrasonic(b, PORT_4).get_sample()

# Grava as configuracoes de terminal para resetar antes de sair
fd = sys.stdin.fileno()
old = termios.tcgetattr(fd)
tty.setcbreak(sys.stdin)

while True:
    tecla=ord(sys.stdin.read(1))
    if tecla==65:
        frente()
        print "frente"
    elif tecla==66:    
        tras() 
        print "tras"
    elif tecla==67:    
        direito()
        print "direita"
    elif tecla==68:    
        esquerdo()
        print "esquerda"
    elif tecla==32:    
        para()
        print "para"
    elif tecla==113:    
        quit()
        print "quit"
    elif tecla==100:
         distancia()
    else:
        print tecla


#	if Touch(b,PORT_1).get_sample() == True :
#		vire_para_direita()
#	if Touch(b,PORT_2).get_sample() == True :
#		vai()
#while True:
	#print 'Filipi Pressed Touch:', Touch(b, PORT_1).get_sample()
#	time.sleep(1)
	


#print 'Sound:', Sound(b, PORT_2).get_sample()
#print 'Light:', Light(b, PORT_3).get_sample()
