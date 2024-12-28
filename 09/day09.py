# AOC day 9

import copy
import numpy as np

with open('input.txt', 'r+') as f:
    data = f.readlines()

data = data[0]
n_id = 0
decompact = []
for i in range(len(data)):
    if i%2 == 0:
        for j in range(int(data[i])):
            decompact.append(n_id)
        n_id += 1
    else:
        for j in range(int(data[i])):
            decompact.append(-1)

def check_sort(dcom):
    space_between = False
    for d in dcom:
        if d == -1:
            space_between = True
        if d != -1 and space_between:
            return False
    return True

def sort_last(dcom):

    last_found, last_id, last = False, len(dcom), 0
    while not last_found:
        last_id += -1
        if dcom[last_id] != -1:
            last_found = True
    last = copy.deepcopy(dcom[last_id])

    print(round(last_id/len(dcom), 3), end='\r')

    i = 0
    placed = False
    while not placed:
        if dcom[i] == -1:
            dcom[i] = last
            dcom[last_id] = -1
            placed = True
        i += 1
    return dcom

# first part
decompact2 = copy.deepcopy(decompact)
#while not check_sort(decompact):
#    decompact = sort_last(decompact)
print('DONE!')
total_sum = 0
#for i in range(len(decompact)):
#    if decompact[i] != -1:
#        total_sum += i*decompact[i]
print(total_sum)

# second part
def find_last(dcom):
    last_found, last_id2, last = False, len(dcom), 0
    while not last_found:
        last_id2 += -1
        if dcom[last_id2] != -1:
            last_found = True
            last = dcom[last_id2]
    first_found, last_id1 = False, last_id2
    while not first_found:
        last_id1 += -1
        if last_id1 < 1:
            first_found = True
            last_id1 = -1
        else:
            if dcom[last_id1] != last:
                first_found = True
    last = copy.deepcopy(dcom[last_id1+1:last_id2+1])
    return last, last_id1+1, last_id2

def find_leftmost(dcom, l):
    i, length = 0, 0
    placed, found = False, False
    while not placed:
        if dcom[i] == -1:
            next_found = False
            length = 0
            while not next_found:
                if dcom[i] == -1:
                    length += 1
                else:
                    next_found = True
                i += 1
                if i >= len(dcom):
                    next_found = True
                    placed = True
            if length >= l:
                placed = True
                found = True
        i += 1
        if i >= len(dcom):
            placed = True
    return i-length-2, i-length+l-3, found

def sort2(dcom):

    end = False
    i = len(dcom)
    while not end:
        last, last_id1, last_id2 = find_last(dcom[:i])
        space_id1, space_id2, f = find_leftmost(dcom[:i], last_id2-last_id1+1)
        if f:
            dcom[last_id1:last_id2+1] = [-1 for i in range(0, last_id2-last_id1+1)]
            dcom[space_id1:space_id2+1] = last
        i = last_id1
        if i <= 0:
            end = True

        print(round(i/len(dcom), 3), end='\r')

    return dcom, end

done = False
check_sum = 0
decompact2, end = sort2(decompact2)
print('DONE!')
for i in range(len(decompact2)):
    if decompact2[i] != -1:
        check_sum += i*decompact2[i]
print(check_sum)