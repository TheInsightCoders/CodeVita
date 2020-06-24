from math import sqrt
n,k = [int(x) for x in input().split()]
cnt = 0
fact = []
# for i in range(1, n+1):
#     if n % i == 0:
#         fact.append(i)
# print(fact[-k])

for i in range(1, int(sqrt(n)+1)):
    if n%i==0:
        fact.append(i)
        fact.append(n//i)
        cnt += 2
fact.sort()
# print(fact)

if cnt > k :
    print(fact[-k])
else:
    print(1)

