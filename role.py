#!/bin/python
#-*-encoding:utf-8-*

# role class
class Role:
	def __init__(self): 
		# open traindata.txt as append mode
		self.trainDataFile = open("traindata.txt", "w")

		# read theta value from theta.txt
		thetaStr = open("theta.txt").readline()
		thetaStr = thetaStr[:len(thetaStr) - 1]
		self.theta = thetaStr.split(" ")
		self.theta = [int(i) for i in self.theta]
		# print self.theta

	# maxmin search
	def search(self, board, currentRole, level = 1): 
		# make movement
		movePosition = self.makeMove(board)

		# evaluate current chessboard
		# black win or white win or reach level 3 or draw, return eval value
		evalValueOfCurrentBoard = self.evaluate(board)
		if(evalValueOfCurrentBoard[2] or evalValueOfCurrentBoard[3] or len(movePosition) == 0 or level == 3):
			return [-1, -1, self.evaluate(board)[0:2]]
		else:
			if currentRole == 0:
				bestResult = [-1, -1, [-10000, None]]
			else:
				bestResult = [-1, -1, [10000, None]]
			for move in movePosition:
				board[move[0]][move[1]] = currentRole
				evalValue = self.search(board, ~currentRole, level + 1)
				if currentRole == 0 and evalValue[2][0] > bestResult[2][0] or \
					 currentRole == -1 and evalValue[2][0] < bestResult[2][0]:
					bestResult[2] = evalValue[2]
					bestResult[1] = move[1]
					bestResult[0] = move[0]
				board[move[0]][move[1]] = 1	# recover

			# save the evaluation value of the successor and the current chessboard, and save the x value as train data
			if(level == 1):
				# self.trainDataFile.write("%d %d\n"%(self.evaluate(board)[0], bestResult[2][0]))
				self.trainDataFile.write("%d %d %s\n"%(evalValueOfCurrentBoard[0], bestResult[2][0], "".join(str(i) + " " for i in bestResult[2][1])))
				# self.trainDataFile.write(str(bestResult[2]))
			return bestResult

	def makeMove(self, board): 
		movePosition = []
		for i in [0, 1, 2]:
			for j in [0, 1, 2]:
				if board[i][j] == 1:
					movePosition.append([i, j])
		return movePosition

	def evaluate(self, board):
		blackWin = False
		whiteWin = False

		# calcu the eigenvalues(x)
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
				if sumOfBlack > 0 and sumOfWhite == 0 :
					# x[sumOfBlack] += sumOfBlack * 30
					if sumOfBlack == 3:
						blackWin = True
					x[sumOfBlack] += 1
				if sumOfWhite > 0 and sumOfBlack == 0 :
					if sumOfWhite == 3:
						whiteWin = True
					# x[sumOfBlack * 2 + 1] -= sumOfWhite * 30
					x[3 + sumOfWhite] += 1

		# summation
		total = 0
		for i in range(len(x)):
			total += x[i] * self.theta[i]
		# print board
		# print "eval : %d x: %s" % (total, str(x))
		return [total, x, blackWin, whiteWin]
