T = int(input())
res = []
for i in range(0, T):
    arr = []
    N = int(input())

    candy = [int(x) for x in input().split()]
    candy.sort()

    while (len(candy)>=2):
        candy.sort()
        sum1 = candy[0] + candy[1]
        arr.append(sum1)
        candy.pop(0)
        candy.pop(0)
        candy.append(arr[-1])
    res.append(sum(arr))

for r in res:
    print(r)


# 1
# 5
# 1 2 3 4 5