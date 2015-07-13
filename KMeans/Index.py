# -*- coding: UTF-8 -*-
"""
@author: nevin47
2015-7-13
Direction:
You should set the Filename and the cluster number as demo
"""
from numpy import *
import kmeans as km

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
    return clusterAssment

##Demo 
FileName = "/Users/nevin47/Desktop/DM&ML&DF/Data Mining/Code/KMeans/test.csv"
Out = KmeansCluster(FileName,4)
print Out