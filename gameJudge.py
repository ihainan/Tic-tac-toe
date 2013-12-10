#!/usr/bin/python
#-*-encoding:utf-8-*-

import sys
from subprocess import *
from chessboard import Chessboard

def sendMessage(proc, message):
	proc.stdin.write(message + "\n")
	proc.stdin.flush()

def receiveMessage(proc):
	message = proc.stdout.readline()
	proc.stdout.flush()
	return message[:len(message) - 1]


if __name__ == '__main__':
	cb = Chessboard(0)	# init a chessboard

	# commuate computer engine wite pipe
	procBlack = Popen('python ./game.py', stdin=PIPE, stdout=PIPE, shell=True)
	procWhite = Popen('python ./game.py', stdin=PIPE, stdout=PIPE, shell=True)

	# send start command to 2 engines
	command = "start black"
	sendMessage(procWhite, command)
	print "send to white : " + command
	result = receiveMessage(procWhite)
	print "receive from white : " + result
	command = "start white"
	sendMessage(procBlack, command)
	print "send to black : " + command
	result = receiveMessage(procBlack)
	print "receive from black : " + result
	mx = int(result.split(" ")[0])
	my = int(result.split(" ")[1])
	cb.move(mx, my)
	cb.drawboard()

	while True:
		# white role's turn
		cb.changePlayRole()
		command = "MOVE %d %d" % (mx, my)
		sendMessage(procWhite, command)
		print "send to white : " + command
		result = receiveMessage(procWhite)
		print "receive from white : " + result
		mx = int(result.split(" ")[0])
		my = int(result.split(" ")[1])
		moveResult = cb.move(mx, my)
		if moveResult == "illegal" or moveResult == "black win" or \
			moveResult == "white win" or moveResult == "draw":
			print moveResult
			sendMessage(procBlack, "quit")
			sendMessage(procWhite, "quit")
			break
		cb.drawboard()

		# black role's turn
		cb.changePlayRole()
		command = "MOVE %d %d" % (mx, my)
		sendMessage(procBlack, command)
		print "send to black : " + command
		result = receiveMessage(procBlack)
		print "receive from black : " + result
		mx = int(result.split(" ")[0])
		my = int(result.split(" ")[1])
		moveResult = cb.move(mx, my)
		if moveResult == "illegal" or moveResult == "black win" or \
			moveResult == "white win" or moveResult == "draw":
			print moveResult
			sendMessage(procBlack, "quit")
			sendMessage(procWhite, "quit")
			break
		cb.drawboard()
