import os
from os import listdir
from os.path import isfile, join
import itertools
import re
from dataclasses import dataclass
import numpy as np
import math
import csv

def ismember(A, B):
    return [np.sum(a == B) for a in A]

def loadpoints(path):
    points_final = []
    f = open(path, 'r')
    c = 1
    for line in f:
        c = c + 1
        if c is 2:
            points = f.readline()
            c = 0
    f.close()
    # points=points.split(",")
    points = re.sub("[^0-9,. ]", "", points)
    points = points.split(',')
    for i in range(0, len(points)):
        points[i] = int(math.ceil(float(points[i])))
    for i in range(0, len(points), 2):
        if [points[i], points[i + 1]] not in points_final:
            points_final.append([points[i], points[i + 1]])  # Point(points[i], points[i + 1]))
    points = []
    return points_final

prefix = ''  # 'l'     #[H frame]
mypath = 'C:/Users/asus/PycharmProjects/ORB1/Resultados-DataBase/saved'
where = [f for f in listdir(mypath) if isfile(join(mypath, f))]
ext= '.txt'
endereco = []
for i in where:
    if ext in i:
        endereco.append(i)
points = []
for i in endereco:
    path = mypath + '/' + i
    points.append(loadpoints(path))


counter=np.zeros(len(points))

c=0
total_number_points=0
for i in points:
    total_number_points = total_number_points + len(i)
    for j in i:
        for k in i:
            if k == j:
                counter[c]=counter[c]+1
    c=c+1

print(sum(counter/total_number_points)/len(counter))