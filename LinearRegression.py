import numpy as np
import csv
import matplotlib.pyplot as mpl

fileName = "xyTrainingData.csv"
points = []
i = 0

#Import CSV file
with open(fileName, 'rb') as csvfile:
	filereader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in filereader:
		points.append([])
		for j in range(0,2): 
			points[i].append(float(row[j]))
		i += 1

#Simple Linear Regression
#Will return values representing line given by y = alpha + beta * x
def simpleLinearRegression(points):
	alpha, beta, xavg, yavg, bdenom, bnum = 0, 0, 0, 0, 0, 0;

	#Find Average x and y
	for i in range(len(points)):
		xavg += points[i][0]
		yavg += points[i][1]
	xavg = xavg / len(points)
	yavg = yavg / len(points)

	#Calculate beta
	for i in range(len(points)):
		bnum += (points[i][0] - xavg) * (points[i][1] - yavg)
		bdenom += (points[i][0] - xavg) ** 2
	beta = bnum / bdenom

	#Calculate alpha
	alpha = yavg - beta * xavg

	#Return alpha, beta
	return alpha, beta

#Execute function on imported points
c = simpleLinearRegression(points)
print c

#Draw results
def drawLine(c, points, reso):
	
	#Break into single arrays
	xarr = []
	yarr = []
	for i in range(len(points)):
		xarr.append(points[i][0])
		yarr.append(points[i][1])	
	
	#Find minimum and maximum x and y
	minx = min(xarr)
	maxx = max(xarr)
	miny = min(yarr)
	maxy = max(yarr)

	#Define x for model
	x = np.arange(minx * 1.10, maxx * 1.10, reso)

	#Plot results
	mpl.plot(x, c[1] * x + c[0], 'r--')
	mpl.plot(xarr, yarr, 'b*')
	mpl.show()

drawLine(c, points, 0.01)