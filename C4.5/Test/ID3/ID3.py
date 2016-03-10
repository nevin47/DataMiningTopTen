# -*- coding: utf-8 -*-
import trees
import treePlotter
fr = open('/Users/nevin47/Desktop/Project/Academic/Code/Python/TopTen_Python/DataMiningTopTen/C4.5/Test/ID3/lenses2.txt')
#导入数据
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
#设置标签
lensesLabels = ['outlook','temperature','humidity','windy']
#生成树
lensesTree = trees.createTree(lenses,lensesLabels)
#画图
treePlotter.createPlot(lensesTree)