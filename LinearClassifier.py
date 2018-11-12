import numpy as np
import csv

fileName = "xyTrainingData.csv"
points = []
i = 0

with open(fileName, 'rb') as csvfile:
	filereader = csv.reader(csvfile, delimiter = ",", quotechar = "|")
	for row in filereader:
		points.append([])
		for j in range(0,2):
			points[i].append(float(row[j]))
		i += 1

print points
