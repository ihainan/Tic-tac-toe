#!/bin/python
#-*-encoding:utf-8-*

# role class
class Role:
	def __init__(self): pass

	# maxmin search
	def search(self, board, currentRole, level = 1): 
		movePosition = self.makeMove(board)
		if(len(movePosition) == 0 or level == 3):
			return [-1, -1, self.evaluate(board)]
		else:
			if currentRole == 0:
				bestResult = [-1, -1, -10000]
			else:
				bestResult = [-1, -1, 10000]
			for move in movePosition:
				board[move[0]][move[1]] = currentRole
				evalValue = self.search(board, ~currentRole, level + 1)
				if currentRole == 0 and evalValue[2] > bestResult[2]:
					bestResult[2] = evalValue[2]
					bestResult[1] = move[1]
					bestResult[0] = move[0]
				if currentRole == -1 and evalValue[2] < bestResult[2]:
					bestResult[2] = evalValue[2]
					bestResult[1] = move[1]
					bestResult[0] = move[0]
				board[move[0]][move[1]] = 1	# recover
			return bestResult

	def makeMove(self, board): 
		movePosition = []
		for i in [0, 1, 2]:
			for j in [0, 1, 2]:
				if board[i][j] == 1:
					movePosition.append([i, j])
		return movePosition

	def evaluate(self, board):
		x = [0 for i in range(7)]
		step = [[1, 1], [-1, 1], [0, 1], [1, 0]]
		startPoint = [[[0, 0]], [[2, 0]], [[i, 0] for i in range(3)], [[0, i] for i in range(3)]]
		for i in range(4):
			for sp in startPoint[i]:
				sx = sp[0]
				sy = sp[1]
				sumOfBlack = 0
				sumOfWhite = 0
				while sx < 3 and sy < 3:
					if board[sx][sy] == 0:
						sumOfBlack += 1
					if board[sx][sy] == -1:
						sumOfWhite += 1
					sx += step[i][0]
					sy += step[i][1]
				# print "sumOfBlack = %d | sumOfWhite = %d" % (sumOfBlack, sumOfWhite)
				if sumOfBlack > 1 and sumOfWhite == 0 :
					x[sumOfBlack] += sumOfBlack * 30
				if sumOfWhite > 1 and sumOfBlack == 0 :
					x[sumOfBlack * 2 + 1] -= sumOfWhite * 30
		return sum(x)
