# -*- coding: UTF-8 -*-
"""
@author: nevin47
2015-7-13
Direction:
You should set the Filename and the cluster number as demo
"""
from numpy import *
import kmeans as km
import matplotlib.pyplot as plt
from pylab import *

#mainFUNC
def KmeansCluster(FileName = "",Num = 3):
    dataSet = []
    fileIn = open(FileName)
    for line in fileIn.readlines():
        lineArr = line.strip().split(',')
        dataSet.append([float(i) for i in lineArr])
    dataSet = mat(dataSet)
    k = Num
    centroids, clusterAssment = km.kmeans(dataSet, k)
    return centroids,clusterAssment

##Demo
CO = [0,0]
for op in range(7):
    if(op!=0 and op!=1):
        print "OP = ",op,'\n'
        FileName = "/Users/nevin47/Desktop/项目/学术/TopTen_Python/DataMiningTopTen/KMeans/Table/PY.csv"
        Center,Out = KmeansCluster(FileName,op)
        # print Out

        dataSet = []
        fileIn = open(FileName)
        for line in fileIn.readlines():
            lineArr = line.strip().split(',')
            dataSet.append([float(i) for i in lineArr])
        dataSet = mat(dataSet)

        Result = km.CalVectorDistance(dataSet,Out)

        SUM = 0
        for i in range(dataSet.shape[0]):
            SUM += km.CalVectorCoefficient(Result,i,op)
        CO.append(SUM/dataSet.shape[0])

print CO

#Draw Pic
y = array(CO)
xlim(2,5)
plot(y)
show()