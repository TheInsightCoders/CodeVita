"""
3
8
2 2 4 3 5 2 6 2 3
3 5 7 4 3 9 3 2 2
1 2 4 2 7 5 3 2 4
"""

from collections import Counter

n = int(input())
t = int(input())
participant = []
l = []
g = []
for i in range(n):
    k = list(map(int, input().split()))
    d = k[-1]
    k.pop()
    w = []
    sum1 = 0
    for i in k:
        q = i * d
        sum1 += q
        w.append(sum1)

    l.append(w)
for i in range(t):
    g.append(list(list(zip(*l))[i]))
for i in range(1, len(g), 2):
    m = max(g[i])
    for j in range(len(g[i])):
        if m == g[i][j]:
            participant.append(j + 1)
res = dict(Counter(participant))
l1 = list(res.values())
l2 = list(res.keys())
print(l2[l1.index(max(l1))])
