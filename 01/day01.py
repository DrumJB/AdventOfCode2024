# AOC day 1

import pandas as pd
import numpy as np

# first part
df = pd.read_csv('input.txt', sep='   ', engine ='python', names=['A', 'B'])
a = np.array(np.sort(df['A']))
b = np.array(np.sort(df['B']))
diff = np.abs(a-b)
print(f"Answer of part 1:      {np.sum(diff)}")

# second part
similar_numbers = []
for n in a:
    sim = 0
    for m in b:
        if n == m:
            sim += 1
    similar_numbers.append(sim)
similar_numbers = np.array(similar_numbers)
print(f"Answer of part 2:      {np.sum(np.multiply(a, similar_numbers))}")