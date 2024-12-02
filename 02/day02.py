# AOC day 2

with open('input.txt', 'rb') as f:
    data = f.readlines()

reports = []
for d in data:
    splitted = str(d).split(" ")
    splitted[0] = splitted[0][2:]
    splitted[-1] = splitted[-1][0:-3]
    for i in range(0, len(splitted)):
        splitted[i] = int(splitted[i])
    reports.append(splitted)

def is_safe(r):
    unsafe = False
    increasing = (r[0]<r[1])
    for i in range(1, len(r)):
        if (r[i-1]<r[i]) != increasing:
            unsafe = True
        if abs(r[i]-r[i-1]) < 1 or abs(r[i]-r[i-1]) > 3:
            unsafe = True
    return not unsafe


# first part & second part
safe = 0
safe2 = 0
for r in reports:
    if is_safe(r):
        safe += 1
    unsafe = True
    for i in range(len(r)):
        if is_safe(r[:i] + r[i+1:]):
            unsafe = False
    if not unsafe: safe2 += 1
print(f"Answer of part 1:       {safe}")
print(f"Answer of part 2:       {safe2}")