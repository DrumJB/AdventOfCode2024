# AOC day 11

with open('input.txt', 'r+') as f:
    data = f.readlines()

stones = [int(x) for x in data[0].split(' ')]

bank = [[], []]

def evolve_stone(s,  b):
    if b == 0:
        return [s]
    else:
        results = []
        if s == 0:
            for a in evolve_stone(1, b-1): results.append(a)
        elif len(str(s))%2 == 0:
            first = int(str(s)[:int(len(str(s))/2)])
            second = int(str(s)[int(len(str(s))/2):])
            for a in evolve_stone(first, b-1): results.append(a)
            for a in evolve_stone(second, b-1): results.append(a)
        else:
            for a in evolve_stone(s*2024, b-1): results.append(a)
        return results
    
def evolve_stone_bank(s, b):
    if b == 0:
        return [s]
    elif s in bank[0]:
        next_steps = bank[1][bank[0].index(s)]
    else:
        next_steps = evolve_stone(s, 5)
        bank[0].append(s)
        bank[1].append(next_steps)
    results = []
    for ns in next_steps:
        for r in evolve_stone_bank(ns, b-1): results.append(r)
    return results

# first part
n_stones = 0
for stone in stones:
    n_stones += len(evolve_stone(stone, 25))
print(n_stones)