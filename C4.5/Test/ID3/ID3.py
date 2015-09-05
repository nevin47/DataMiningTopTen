# -*- coding: utf-8 -*-
import trees
import treePlotter
fr = open('/Users/nevin47/Desktop/项目/学术/TopTen_Python/DataMiningTopTen/C4.5/Test/ID3/lenses.txt')
#导入数据
lenses = [inst.strip().split('\t') for inst in fr.readlines()]
#设置标签
lensesLabels = ['age','prescript','astigmatic','tearRate']
#生成树
lensesTree = trees.createTree(lenses,lensesLabels)
#画图
treePlotter.createPlot(lensesTree)