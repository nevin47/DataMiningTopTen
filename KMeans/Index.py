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
    return centroids,clusterAssment

##Demo 
# FileName = "/Users/nevin47/Desktop/项目/学术/TopTen_Python/DataMiningTopTen/KMeans/Table/FINAL.csv"
# Center,Out = KmeansCluster(FileName,3)
# # print Out
#
# dataSet = []
# fileIn = open(FileName)
# for line in fileIn.readlines():
#     lineArr = line.strip().split(',')
#     dataSet.append([float(i) for i in lineArr])
# dataSet = mat(dataSet)
# # C = transpose(mat(Center[1]))
# # D = dataSet[1]
# # print D*C
# Result = km.CalVectorDistance(dataSet,Out)
# # print Result[:,0,:]
# SUM = 0
# for i in range(dataSet.shape[0]):
#     SUM += km.CalVectorCoefficient(Result,i,3)
# print SUM/dataSet.shape[0]
# # print km.CalVectorCoefficient(Result,0,3)