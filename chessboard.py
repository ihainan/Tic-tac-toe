#!/bin/python
#-*-encoding:utf-8-*

# chessboard class
class Chessboard:
	def __init__(self, currentRole): 
		self.currentRole = currentRole
		self.board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]

	def changePlayRole(self):
		self.currentRole = ~self.currentRole	

	def move(self, positionX, positionY): 
		if positionX < 0 or positionX > 2 or \
			positionY < 0 or positionY > 2 or \
			self.board[positionX][positionY] != 1:
			self.changePlayRole()
			return 'illegal'
		self.board[positionX][positionY] = self.currentRole
		step = [[1, 1], [-1, 1], [0, 1], [1, 0]]
		startPoint = [[[0, 0]], [[2, 0]], [[i, 0] for i in range(3)], [[0, i] for i in range(3)]]
		for i in range(4):
			for sp in startPoint[i]:
				sx = sp[0]
				sy = sp[1]
				sumOfBlack = 0
				sumOfWhite = 0
				while sx < 3 and sy < 3:
					if self.board[sx][sy] == 0:
						sumOfBlack += 1
					if self.board[sx][sy] == -1:
						sumOfWhite += 1
					sx += step[i][0]
					sy += step[i][1]
				if sumOfBlack == 3:
					return "black win"
				if sumOfWhite == 3:
					return "white win"
	
		l = []
		for i in range(3):
			l.extend(self.board[i])
		if not 1 in l:
			return "draw"
		return ""


	def reset(self): 
		self.board = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
	
	def drawboard(self):
		for i in self.board:
			for j in i:
				print "%2d" % (j),
			print ""
		print ""


