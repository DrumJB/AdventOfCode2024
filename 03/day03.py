# AOC day 3

import numpy as np

with open('input.txt', 'r+') as f:
    data = f.readlines()

# first part
total_sum = 0
def multiply_line(data_string):
    sum = 0
    commands = data_string.split('mul')
    for c in commands:
        if len(c) > 0:
            if c[0] == '(':
                temp_string = c[1:]
                if ')' in temp_string:
                    temp_string = temp_string.split(')')[0]
                    a = temp_string.split(',')[0]
                    if len(temp_string.split(','))>1:
                        b = temp_string.split(',')[1]
                        if a.isdigit() and b.isdigit():
                            sum += int(a)*int(b)
    return sum

for d in data:
    total_sum += multiply_line(d)

# second part
tot_string = ''
for d in data:
    tot_string += d
donts = tot_string.split("don't()")
dos = [donts[0]]
for dont in donts:
    splitted = dont.split("do()")
    if len(splitted) > 1:
        for sp in splitted[1:]:
            dos.append(sp)
print(dos)
total_sum2 = 0
for d in dos:
    total_sum2 += multiply_line(d)

print(f"Answer of part 1:       {total_sum}")
print(f"Answer of part 2:       {total_sum2}")