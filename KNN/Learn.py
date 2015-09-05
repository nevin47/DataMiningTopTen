#coding:utf-8
__author__ = 'nevin47'

import numpy as np
import operator

def CreatDataSet():
    '''
    生成数据集函数
    :return:
    '''
    group = np.array([[1.0,1.1],[1.0,1.0],[0,0],[0,0.1]])
    labels = ['A','A','B','B']
    return group,labels

def CalDistance(TargetVector, CompareVector):
    '''
    计算两个点之间的距离
    :param TargetVector:需要计算点 'numpy.array'
    :param CompareVector:对比点 'numpy.array'
    :return:distance 距离 'numpy.float64'
    '''
    SQdistance = (TargetVector - CompareVector)**2
    SQdistance = SQdistance.sum()
    distance = SQdistance**0.5
    return distance


a = np.array([2,3,4])
b = np.array([4,5,6])
print type(CalDistance(a,b))