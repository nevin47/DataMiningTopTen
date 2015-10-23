# -*- coding: utf-8 -*-
import Apriori.apriori as APR
import SVM.SVM as SVM
import KMeans.Index as KM

#Apriori Demo
APR.AprioriRun("/Users/nevin47/Desktop/项目/学术/TopTen_Python/DataMiningTopTen/Apriori/test.csv",0.15,0.6)

#Kmeans Demo
# FileName = "/Users/nevin47/Desktop/项目/学术/TopTen_Python/DataMiningTopTen/KMeans/Table/FINAL.csv"
# Center,Out = KM.KmeansCluster(FileName,3)
# print "The result is :",Out,"\n"
# print "The center is:\n",Center


