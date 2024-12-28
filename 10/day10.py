# AOC day 10

with open('input.txt', 'r+') as f:
    data = f.readlines()

map = []
for d in data:
    temp_list = []
    for a in d[:-1]:
        temp_list.append(int(a))
    map.append(temp_list)

def find_next_node(x, y):
    n = map[x][y]
    if n == 9:
        return [[x, y]]
    results = []
    for a in range(-1, 2):
        if -1<x+a<len(map):
            if map[x+a][y] == n+1:
                r = find_next_node(x+a, y)
                for res in r:
                    if res not in results:
                        results.append(res)
        if -1<y+a<len(map[0]):
            if map[x][y+a] == n+1:
                r = find_next_node(x, y+a)
                for res in r:
                    if res not in results:
                        results.append(res)
    return results

# first part
total_trailheads_score = 0
for n in range(len(map)):
    for m in range(len(map[0])):
        if map[n][m] == 0:
            tot_res = find_next_node(n, m)
            total_trailheads_score += len(tot_res)
print(total_trailheads_score)