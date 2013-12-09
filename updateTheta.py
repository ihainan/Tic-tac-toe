#!/bin/python
#-*-encoding:utf-8-*

# learning rate
lr = 0.01
times = 1

# open traindata.txt as append mode
trainDataFile = open("traindata.txt", "r")
trainDataSet = []
while True:
	trainDataStr = trainDataFile.readline()
	if not trainDataStr: break
	trainDataStr = trainDataStr[:len(trainDataStr) - 2]
	trainData = trainDataStr.split(" ")
	trainDataSet.append([int(i) for i in trainData])
print trainDataSet

# read theta value from theta.txt
thetaStr = open("theta.txt").readline()
thetaStr = thetaStr[:len(thetaStr) - 1]
theta = thetaStr.split(" ")
theta = [int(i) for i in theta]
print theta

# train
for t in range(times):
	for data in trainDataSet:
		trainValue = data[0]
		objectValue = data[1]
		x = data[2:]
		for i in range(len(theta)):
			theta[i] = theta[i] + lr * (objectValue - trainValue) * x[i]

print theta
# save theta
