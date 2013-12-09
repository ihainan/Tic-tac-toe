#!/bin/python
#-*-encoding:utf-8-*
import random
from chessboard import Chessboard
from role import Role

# main
rl = Role()		# init the computer role
while True:
	command = raw_input("Input command : ").split(" ")

	if command[0].upper() == "QUIT" or command[0].upper() == "Q":	# quit the game
		print "Bye"
		break

	if command[0].upper() == "START":	# play a new game
		if len(command) == 1 or \
		   (command[1].upper() != "BLACK" \
		   and command[1].upper() != "WHITE"):
			print "please tell me which role you want to play"
			continue
		print "Start a new game"
		if command[1].upper() == "BLACK":
			# wait the opponent player to make a move
			cb = Chessboard(-1)	# black first always
			pass
		else:
			# computer make a movement at the begin
			cb = Chessboard(0)	# black first always
			movePosition = rl.search(cb.board, cb.currentRole)
			moveResult = cb.move(movePosition[0], movePosition[1])
			cb.drawboard()
			if moveResult != "":
				print moveResult
				continue
		continue
		
	if command[0].upper() == "MOVE":	# make a move
		if len(command) != 3:
			continue

		# opponent player's turn
		cb.changePlayRole()
		moveResult = cb.move(int(command[1]), int(command[2]))
		cb.drawboard()
		if moveResult != "":
			print moveResult
			continue

		# computer's turn
		cb.changePlayRole()
		movePosition = rl.search(cb.board, cb.currentRole, 1)	# search for best movement
		moveResult = cb.move(movePosition[0], movePosition[1])
		print "Computer : (%d, %d) => %d" % (movePosition[0], movePosition[1], movePosition[2])
		cb.drawboard()
		if moveResult != "":
			print moveResult
			continue
		continue

	if command[0].upper() == "TEST":	# test module
		cb = Chessboard(0)
		cb.board = [[0, -1, 0], [-1, -1, 0], [-1, -1, 0]]
		cb.board = [[random.choice([-1, 0, 1]),random.choice([-1, 0, 1]), random.choice([-1, 0, 1])] for i in range(3)]
		cb.drawboard()
		print rl.evaluate(cb.board)
	

