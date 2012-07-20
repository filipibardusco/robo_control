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
def f():
	motor_esquerdo.run(100)
	motor_direito.run(100)

# BACKWARD
def b():
	motor_esquerdo.run(-100)
	motor_direito.run(-100)

# STOP
def s():
	motor_direito.idle()
	motor_esquerdo.idle()

# RIGHT
def r():
	motor_direito.run (100)
	motor_esquerdo.run(80)

# LEFT
def l():
	motor_direito.run (80)
	motor_esquerdo.run (100)

while True:
    tecla=ord(sys.stdin.read(1))
    if tecla==65:
        f()
        print "frente"
    elif tecla==66:    
        b() 
        print "tras"
    elif tecla==67:    
        r()
        print "direita"
    elif tecla==68:    
        l()
        print "esquerda"
    elif tecla==32:    
        s()
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
