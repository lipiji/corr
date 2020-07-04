import numpy as np
import pandas as pd

A = np.random.randint(1, 100, 10)
B = A * 0.1
C = A - 1

data = pd.DataFrame({'A':A, 
                     'B':B,
                     'C':C})

print(data)
print(data.corr('pearson'))
print(data.corr('kendall'))
print(data.corr('spearman'))

scores = []
r = []
f = []
i = []
with open("score.txt") as fi:
    for line in fi:
        line = line.strip()
        if line:
            scores.append(float(line))
with open("human_avg.txt") as fi:
    for line in fi:
        line = line.strip()
        if line:
            fs = line.split()
            if len(fs) != 3:
                print("error")
                continue
            r.append(float(fs[0]))
            f.append(float(fs[1]))
            i.append(float(fs[2]))

assert len(scores) == 1800
assert len(r) == len(scores)

data = pd.DataFrame({'Score':scores, '相关性':r, '流畅度':f, '丰富度':i})
print('pearson:')
print(data.corr('pearson'))
print()
print('kendall')
print(data.corr('kendall'))
print()
print('spearman')
print(data.corr('spearman'))


