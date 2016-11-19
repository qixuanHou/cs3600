from NeuralNetUtil import buildExamplesFromCarData,buildExamplesFromPenData
from NeuralNet import buildNeuralNet
import cPickle 
from math import pow, sqrt

def average(argList):
    return sum(argList)/float(len(argList))

def stDeviation(argList):
    mean = average(argList)
    diffSq = [pow((val-mean),2) for val in argList]
    return sqrt(sum(diffSq)/len(argList))

penData = buildExamplesFromPenData() 
def testPenData(hiddenLayers = [40]):
    return buildNeuralNet(penData,maxItr = 200, hiddenLayerList =  hiddenLayers)

carData = buildExamplesFromCarData()
def testCarData(hiddenLayers = [40]):
    return buildNeuralNet(carData,maxItr = 200,hiddenLayerList =  hiddenLayers)




pen = []
car = []
for i in range(5):
	penTest = testPenData()
	print penTest
	pen.append(penTest[1])

for i in range(5):
	carTest = testCarData()
	print carTest
	car.append(carTest[1])
print "Pen:", pen
print "Max:", max(pen)
print "Min:", min(pen)
print "Average:", average(pen)
print "Std Dev:", stDeviation(pen)

print "Car:", car
print "Max: ", max(car)
print "Min:", min(car)
print "Average:", average(car)
print "Std Dev:", stDeviation(car)
