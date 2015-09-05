# -*- coding: UTF-8 -*-

from numpy import *
import time

#Begin of the algorithm KMEANS
# calculate Euclidean distance
def euclDistance(vector1, vector2):
	return sqrt(sum(power(vector2 - vector1, 2)))

# init centroids with random samples
def initCentroids(dataSet, k):
	numSamples, dim = dataSet.shape
	centroids = zeros((k, dim))
	for i in range(k):
		index = int(random.uniform(0, numSamples))
		centroids[i, :] = dataSet[index, :]
	return centroids

# k-means cluster
def kmeans(dataSet, k):
	numSamples = dataSet.shape[0]
	# first column stores which cluster this sample belongs to,
	# second column stores the error between this sample and its centroid
	clusterAssment = mat(zeros((numSamples, 2)))
	clusterChanged = True

	## step 1: init centroids
	centroids = initCentroids(dataSet, k)

	while clusterChanged:
		clusterChanged = False
		## for each sample
		for i in xrange(numSamples):
			minDist  = 100000.0
			minIndex = 0
			## for each centroid
			## step 2: find the centroid who is closest
			for j in range(k):
				distance = euclDistance(centroids[j, :], dataSet[i, :])
				if distance < minDist:
					minDist  = distance
					minIndex = j

			## step 3: update its cluster
			if clusterAssment[i, 0] != minIndex:
				clusterChanged = True
				clusterAssment[i, :] = minIndex, minDist**2

		## step 4: update centroids
		for j in range(k):
			pointsInCluster = dataSet[nonzero(clusterAssment[:, 0].A == j)[0]]
			centroids[j, :] = mean(pointsInCluster, axis = 0)

	print 'Congratulations, cluster complete!'
	return centroids, clusterAssment
#END of the algorithm KMEANS

#Begin of the algorithm Silhouette Coefficient
# calculate Profile Coefficient
#TODO:继续完善

def CalVectorDistance(dataSet, clusterAssment):
	'''
	计算每个点之间相对距离
	:param dataSet:原始数据集
	:param clusterAssment:分类情况
	:return:n*n*2三位矩阵,n:=点个数
	'''
	numSamples = dataSet.shape[0]
	outarray = []
	for i in xrange(numSamples):
		tempDis = []
		for j in xrange(numSamples):
			vector1 = dataSet[i,:]
			vector2 = dataSet[j,:]
			Distance = euclDistance(vector1,vector2)
			Assment = clusterAssment[i,0]
			inputData = array([Distance,Assment])
			tempDis.append(inputData)
		outarray.append(tempDis)
	return array(outarray)

def CalVectorCoefficient(outarray,num,k):
	'''特定点的轮廓系数计算函数
	:param outarray:聚类结果集
	:param num:点编号
	:param k:分类数
	:return:si点的轮廓系数
	'''
	TargetMatrix = outarray[:,num,:]
	numSamples = TargetMatrix.shape[0]
	numAssment = TargetMatrix[num,1]
	# init the NPArray to save the data of Sum and k Count
	SumArray = zeros(k)
	Count = zeros(k)
	for i in xrange(numSamples):
		for j in range(k):
			tempSum = 0
			if(TargetMatrix[i,1] == j and TargetMatrix[i,0] != 0):
				SumArray[j] += TargetMatrix[i,0]
				Count[j] += 1
	AVG = SumArray/Count
	newAVG = []
	for i in range(AVG.shape[0]):
		if(i != numAssment):
			newAVG.append(AVG[i])
	ai = AVG[numAssment]
	bi = min(newAVG)
	si = (bi - ai) / max([ai,bi])
	return si


#END of the algorithm Silhouette Coefficient