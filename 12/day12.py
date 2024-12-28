# AOC day 12

import numpy as np

with open('input.txt', 'r+') as f:
    data = f.readlines()

map = []
for d in data:
    row = []
    for x in d[:-1]:
        row.append(x)
    map.append(row)

accounted = np.zeros((len(map), len(map[0])))

clusters = []

def find_neighbor(x, y):
    type = map[x, y]
    near, result = [], []
    for a in (-1, 2):
        for b in (-1, 2):
            if -1<x+a<len(map) and -1<y+b<len(map[0]):
                if map[x+a][y+b] == type:
                    near.append([x+a], [y+b])
    for n in near:
        res = find_neighbor(n[0], n[1])
        for r in res:
            if r not in result:
                result.append(r)
    
    return result

for i in range(len(map)):
    for j in range(len(map[0])):
        if not accounted[i][j]:
            cluster = find_neighbor(i, j)