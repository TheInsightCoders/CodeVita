test = int(input())

while (test > 0):
    P = input()
    S = input()
    list1 = []
    for i in S:
        list1.append(P.find(i))
    list1.sort()
    for i in list1:
        print(P[i], end='')
    if test > 1:
        print('')
    test -= 1
