s,t = [int(x) for x in input().split()]
c = 0
result = []
samples = [int(x) for x in input().split()]

for i in range (t):
    r1, r2 = [int(x) for x in input().split()]
    for j in samples:
        if ((j >= r1) and (j <= r2)):
            c +=1
    result.append(c)
    c=0

for i in result:
    print(i, end =' ')

"""
20 3
921 107 270 631 926 543 589 520 595 93 873 424 759 537 458 614 725 842 575 195
1 100
50 600
1 1000
Output :
1 12 20

10 2
345 604 321 433 704 470 808 718 517 811
300 350
400 700

Output :
2 4
"""