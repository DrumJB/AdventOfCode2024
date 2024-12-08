# AOC day 8

with open('input.txt', 'r+') as f:
    data = f.readlines()

def get_map(data):
    antennas = dict()

    for a in range(len(data)):
        for b in range(len(data[0])-1):
            if data[a][b] != '.':
                if data[a][b] in antennas.keys():
                    antennas[data[a][b]].append([a, b])
                else:
                    antennas.update({data[a][b]: [[a,b]]})
    return antennas

def find_antinodes(ants):
    antinodes = []
    for a in range(len(ants)):
        for b in range(a+1, len(ants)):
            xdiff = ants[a][0] - ants[b][0]
            ydiff = ants[a][1] - ants[b][1]
            antinode1 = [ants[a][0] + xdiff, ants[a][1] + ydiff]
            antinode2 = [ants[b][0] - xdiff, ants[b][1] - ydiff]
            antinodes.append(antinode1)
            antinodes.append(antinode2)
    return antinodes

def find_antinodes2(ants, xlim, ylim):
    antinodes = []
    for a in range(len(ants)):
        for b in range(a+1, len(ants)):
            xdiff = ants[a][0] - ants[b][0]
            ydiff = ants[a][1] - ants[b][1]
            for k in range(0, xlim):
                a1 = [ants[a][0] + k*xdiff, ants[a][1] + k*ydiff]
                a2 = [ants[b][0] - k*xdiff, ants[b][1] - k*ydiff]
                if (-1<a1[0]<xlim) and (-1<a1[1]<ylim):
                    antinodes.append(a1)
                if (-1<a2[0]<xlim) and (-1<a2[1]<ylim):
                    antinodes.append(a2)
    return antinodes

ant_data = get_map(data)
xlim, ylim = len(data), len(data[0][:-1])
total_antnd, total_antnd2 = [], []
for k in ant_data.keys():
    antind = find_antinodes(ant_data[k])
    antind2 = find_antinodes2(ant_data[k], xlim, ylim)
    for a in antind:
        if -1<a[0]<xlim and -1<a[1]<ylim:
            if a not in total_antnd:
                total_antnd.append(a)
    for a in antind2:
        if a not in total_antnd2:
            total_antnd2.append(a)
print(len(total_antnd))
print(len(total_antnd2))