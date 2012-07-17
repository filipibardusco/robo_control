#!/usr/bin/env python

import nxt.locator
from nxt.sensor import *
import time
from nxt.motor import *

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
	comando = raw_input("Digite o comando para controlar o robo: ")
	print "you entered ", comando
	try:
		eval(comando+"()")
	except:
		print "comando esta errado"


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
