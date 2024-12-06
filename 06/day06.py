# AOC day 6

# the first code didn't work... I don't know yet why...

with open('input.txt', 'r+') as f:
    data = f.readlines()

map = []
position = []
for d in range(len(data)):
    row = []
    for x in range(len(data[d])):
        if data[d][x] == '#':
            row.append(True)
        elif data[d][x] == '^':
            position = [d, x]
            row.append(False)
        elif data[d][x] == '.':
            row.append(False)
    map.append(row)

def find_path(map, dir, pos, return_pos=False):
    in_cycle = False
    out_of_map = False
    xl = len(map)
    yl = len(map[0])
    seen = []
    positions = [pos]
    while not out_of_map and not in_cycle:
        next_pos = [pos[0]+dir[0], pos[1]+dir[1]]
        if (-1<next_pos[0]<xl) and (-1<next_pos[1]<yl):
            if map[next_pos[0]][next_pos[1]]:
                if dir==[1, 0]: dir = [0, -1]
                elif dir==[0,-1]: dir = [-1, 0]
                elif dir==[-1,0]: dir = [0,1]
                elif dir==[0,1]: dir = [1,0]
                if [pos, dir] not in seen:
                    seen.append([pos, dir])
                else:
                    in_cycle = True
            else:
                pos = next_pos
                if return_pos:
                    if pos not in positions:
                        positions.append(pos)
        else:
            out_of_map = True
    if return_pos:
        return positions
    return in_cycle

path = find_path(map, [-1, 0], position, return_pos=True)
print(f"Answer of part 1:       {len(path)}")
total_cycles = 0
for p in path[1:]:
    map[p[0]][p[1]] = True
    if find_path(map, [-1, 0], position):
        total_cycles += 1
    map[p[0]][p[1]] = False
print(f"Answer of part 2:       {total_cycles}")