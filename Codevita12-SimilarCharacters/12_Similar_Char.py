N = int(input())
S = input()
Q = int(input())
result =[]
for i in range(Q):
    P = int(input())
    result.append(S[:P-1].count(S[P-1]))

for j in range (len(result)-1):
    print(result[j])
print(result[-1], end = '')   # avoid presentation error

"""
9
abacsddaa
2
9
3
"""
