# AOC day 05

import copy as cp

with open('input.txt', 'r+') as f:
    data = f.readlines()

# first part
rules_str, rules, updates_str, updates = [], [], [], []
rules_end = False
for d in data:
    if d == '\n':
        rules_end = True
    elif not rules_end:
        rules_str.append(d[:-1])
    else:
        updates_str.append(d[:-1])
for r in range(len(rules_str)):
    rules.append([int(s) for s in rules_str[r].split('|')])
for u in range(len(updates_str)):
    updates.append([int(s) for s in updates_str[u].split(',')])

def check_rule(update, rule):
    position = 0
    correct = True
    for u in range(len(update)):
        if update[u] == rule[0]:
            position = u
    for i in range(0, position):
        if update[i] == rule[1]:
            correct = False
    return correct

def check_update(update, rules):

    correct = True
    
    for r in rules:
        if not check_rule(update, r):
            correct = False
    return correct

sum = 0
for u in updates:
    if check_update(u, rules):
        sum += u[int(len(u)/2)]

print(f"Answer of part 1:       {sum}")

# second part
sum2 = 0
def correct_rule(update, rule):
    corrected = update
    if not check_rule(update, rule):
        position1, position2 = 0, 0
        for u in range(len(update)):
            if update[u] == rule[0]:
                position1 = u
            if update[u] == rule[1]:
                position2 = u
        for p in range(position2, position1):
            corrected[p] = update[p+1]
        corrected[position1-1] = rule[0]
        corrected[position1] = rule[1]

    return corrected        

def correct_update(update, rules):

    corrected = cp.deepcopy(update)
    while not check_update(corrected, rules):
        for r in rules:
            corrected = correct_rule(corrected, r)
    return corrected

for u in updates:
    c = correct_update(u, rules)
    if not c == u:
        sum2 += c[int(len(c)/2)]

print(f"Answer of part 2:       {sum2}")