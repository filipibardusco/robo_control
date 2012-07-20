#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
import time
from nxt.motor import *
import sys
import tty
tty.setcbreak(sys.stdin)

metodo = nxt.locator.Method(bluetooth=True)
print"procurando robo..."
b = nxt.locator.find_one_brick(method=metodo)
print"robo localizado"
motor_esquerdo = Motor(b, PORT_B)
motor_direito = Motor(b, PORT_C)

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
	motor_direito.run (100)
	motor_esquerdo.run(80)

# LEFT
def esquerdo():
	motor_direito.run (80)
	motor_esquerdo.run (100)

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
#print 'Ultrasonic:', Ultrasonic(b, PORT_4).get_sample()
