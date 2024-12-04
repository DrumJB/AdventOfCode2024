# AOC day 4

with open('input.txt', 'r+') as f:
    data = f.readlines()

# part one

count = 0

table = []
for d in data:
    row = []
    for ch in d:
        row.append(ch)
    table.append(row[:-1])

for y in range(0, len(table)):
    for x in range(0, len(table[0])):
        
        # in row
        if x < len(table[0])-3:
            if (table[y][x]+table[y][x+1]+table[y][x+2]+table[y][x+3] == 'XMAS') or (table[y][x]+table[y][x+1]+table[y][x+2]+table[y][x+3] == 'SAMX'):
                count += 1
        # in column
        if y < len(table)-3:
            if (table[y][x]+table[y+1][x]+table[y+2][x]+table[y+3][x] == 'XMAS') or (table[y][x]+table[y+1][x]+table[y+2][x]+table[y+3][x] == 'SAMX'):
                count += 1
        # in diagonal to right 
        if x < len(table[0])-3 and y < len(table)-3:
            if (table[y][x]+table[y+1][x+1]+table[y+2][x+2]+table[y+3][x+3] == 'XMAS') or (table[y][x]+table[y+1][x+1]+table[y+2][x+2]+table[y+3][x+3] == 'SAMX'):
                count += 1
        # in diagonal to left
        if x > 2 and y < len(table)-3:
            if (table[y][x]+table[y+1][x-1]+table[y+2][x-2]+table[y+3][x-3] == 'XMAS') or (table[y][x]+table[y+1][x-1]+table[y+2][x-2]+table[y+3][x-3] == 'SAMX'):
                count += 1

print(f"Answer of part 1:       {count}")

# second part
count = 0
for y in range(1, len(table)-1):
    for x in range(1, len(table[0])-1):

        if (table[y-1][x-1]+table[y][x]+table[y+1][x+1] == 'MAS') or (table[y-1][x-1]+table[y][x]+table[y+1][x+1] == 'SAM'):
            if (table[y-1][x+1]+table[y][x]+table[y+1][x-1] == 'MAS') or (table[y-1][x+1]+table[y][x]+table[y+1][x-1] == 'SAM'):
                count += 1

print(f"Answer of part 2:       {count}")