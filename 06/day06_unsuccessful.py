# AOC day 6

import copy

with open('input.txt', 'r+') as f:
    data = f.readlines()

# first part
position = [0, 0]
map = []
for d in range(len(data)):
    row = []
    for x in range(len(data[0])-1):
        if data[d][x] == '^':
            position = [d, x]
            row.append(False)
        elif data[d][x] == '#':
            row.append(True)
        else:
            row.append(False)
    map.append(row)

in_map = True
direction = [-1, 0]
positions = [position]
while in_map:
    try:
        next_pos = [position[0]+direction[0], position[1]+direction[1]]
        if map[next_pos[0]][next_pos[1]]:
            if direction == [1, 0]:
                direction = [0,-1]
            elif direction == [0, -1]: 
                direction = [-1,0]
            elif direction == [-1, 0]: 
                direction = [0,1]
            elif direction == [0, 1]: 
                direction = [1,0]
        else:
            position = next_pos
            if position not in positions:
                positions.append(position)
    except:
        in_map = False

print(len(positions))

# part two

position = [0, 0]
map = []
for d in range(len(data)):
    row = []
    for x in range(len(data[0])-1):
        if data[d][x] == '^':
            position = [d, x]
            row.append(False)
        elif data[d][x] == '#':
            row.append(True)
        else:
            row.append(False)
    map.append(row)
init_pos = copy.deepcopy(position)

def try_exit(custom_map, position):
    in_cycle = False
    in_map = True
    direction = [-1, 0]
    change_positions = []
    while in_map and not in_cycle:
        try:
            next_pos = [position[0]+direction[0], position[1]+direction[1]]
            if custom_map[next_pos[0]][next_pos[1]]:
                if [position, direction] in change_positions:
                    in_cycle = True
                    print(position, direction, change_positions)
                else:
                    change_positions.append([position, direction])
                if direction == [1, 0]:
                    direction = [0,-1]
                elif direction == [0, -1]: 
                    direction = [-1,0]
                elif direction == [-1, 0]: 
                    direction = [0,1]
                elif direction == [0, 1]: 
                    direction = [1,0]
            else:
                position = next_pos
        except IndexError:
            in_map = False
    return in_cycle

possible_obstacles = 0
for p in range(100):
    d = positions[p][0]
    x = positions[p][1]
    if [d, x] != init_pos:
        #print(round(p/len(positions), 3), end='\r')
        map[d][x] = True
        pos = init_pos
        if try_exit(map, pos):
            print(d, x)
            possible_obstacles += 1
        map[d][x] = False
print('DONE!')
print(possible_obstacles)