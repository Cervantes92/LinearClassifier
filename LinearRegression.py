import numpy as np
import csv

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

#Classifier function
def linearClassifier(points):

#Score function
def score(points):

#Loss function
def loss(value, index, points):

#Weight matrix
