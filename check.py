import os
from os import listdir
from os.path import isfile, join
import itertools
import re
from dataclasses import dataclass
import numpy as np
import math
import csv

final = []


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


def ismember(A, B):
    return [np.sum(a == B) for a in A]


def compare(db, notdb):
    counter = np.zeros((len(db)))
    indb = np.array(db)
    notindb = np.array(notdb)
    size = np.array([round(np.size(i)*0.6) for i in [indb[x] for x in range(0, len(indb))]])
    c = 0
    for x in notindb:
        for y in indb:
            counter[c] = np.count_nonzero(ismember(x, y))
            c = c + 1
    counter = np.ndarray.tolist(counter)
    final.append(counter)
    a = counter / size
    if np.sum(np.where(size < max(counter))):
        # print(counter)
        return np.where(a == max(a))[0][0]#np.where(size == max(size[np.where(size < max(counter))[0] - 1]))[0][0]  # counter.index(max(counter))
    else:
        # print(max(counter))
        return -1


prefix = ''  # 'l'     #[H frame]
mypath = 'C:/Users/asus/PycharmProjects/ORB1/Resultados-DataBase/saved'
ext = '.txt'
where = [f for f in listdir(mypath) if isfile(join(mypath, f))]
endereco = []
for i in where:
    if ext in i:
        endereco.append(i)
points = []
for i in endereco:
    path = mypath + '/' + i
    points.append(loadpoints(path))

loadeddbpoints = points

where1 = ['Speckle_22Apr/Paper_B','Speckle_22Apr/Paper_B'] #'Speckle_22Apr/Paper_A_dif','Speckle_22Apr/Paper_A_desl','Speckle_22Apr/Paper_A','Speckle_22Apr/Paper_B','Speckle_22Apr/Paper_B_desl','Speckle_22Apr/Paper_B_dif']
prefix = ''  # 'l'     #[H frame]
list2 = []
endereco.append('Not in DB')
points = []
results = []
positive = []
for where in where1:
    mypath = 'C:/Users/asus/PycharmProjects/ORB1/Resultados-' + where
    list1 = [f for f in listdir(mypath) if isfile(join(mypath, f))]
    for i in list1:
        if '.txt' in i:
            list2.append(i)
    for i in list2:
        path = mypath + '/' + i
        points.append(loadpoints(path))
        # compare(loadeddbpoints, points)
        results.append(endereco[compare(loadeddbpoints, points)])
        print('Foi encontrado na BD ---> ' + str(where) + ' > ' + str(i) + ', no estado ' + str(results[-1]))
        points = []
    list1 = []
    list2 = list1

count_A = [x for x in results if 'A' in x]
count_B = [x for x in results if 'B ' in x]
count_null = [x for x in results if 'Not' in x]

print('A: ' + str(len(count_A)) + '\tB: ' + str(len(count_B)) + '\tNot in DB: ' + str(len(count_null)))

with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(final)
