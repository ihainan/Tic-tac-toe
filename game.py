#!/usr/bin/python
#-*-encoding:utf-8-*

import random
from chessboard import Chessboard
from role import Role
import sys

def sendMessage(message):
	sys.stdout.write(message + "\n")
	sys.stdout.flush()

def receiveMessage():
	message = sys.stdin.readline()
	sys.stdin.flush()
	return message[:len(message) - 1]

rl = Role()		# init the computer role
while True:
	# receive command from judge program
	command = receiveMessage()
	command = command.split()
	
	if command[0].upper() == "QUIT" or command[0].upper() == "Q":	# quit the game
		sendMessage("bye")
		exit()

	elif command[0].upper() == "START":	# play a new game
		if command[1].upper() == "BLACK":
			# wait the opponent player to make a move
			sendMessage("ok")
			cb = Chessboard(-1)	# black first always
			continue
		else:
			# computer make a movement at the begin
			cb = Chessboard(0)	# black first always
			movePosition = rl.search(cb.board, cb.currentRole)
			moveResult = cb.move(movePosition[0], movePosition[1])
			sendMessage("%d %d"%(movePosition[0], movePosition[1]))
		continue
	
	if command[0].upper() == "MOVE":	# make a move
		# opponent player's turn
		cb.changePlayRole()
		moveResult = cb.move(int(command[1]), int(command[2]))

		# computer's turn
		cb.changePlayRole()
		movePosition = rl.search(cb.board, cb.currentRole, 1)	# search for best movement
		moveResult = cb.move(movePosition[0], movePosition[1])
		sendMessage("%d %d" % (movePosition[0], movePosition[1]))
		continue
