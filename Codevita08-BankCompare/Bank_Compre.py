p = int(input())  # p principal (Loan Amount)
t = int(input())  # t Total Tenure (in years)
bank =[]
for k in range (2):
    n = int(input())  # No. of slabs
    sum1 = 0
    for i in range (n):
        yrs, slab = [float(x) for x in input().split()]
        yrs = int(yrs)
        sq=(1+slab)**(yrs * 12)
        emi= (p * (slab)) / (1-1 / sq)  # formula
        sum1= sum1 + emi
    bank.append(sum1)  # store result
# print(bank)
if (bank[0] < bank[1]):  # print output
    print("Bank A",end='')
else:
    print("Bank B",end='')

"""
10000
20
3
5 9.5
10 9.6
5 8.5
3
10 6.9
5 8.5
5 7.9
Output: Bank B

500000
26
3
13 9.5
3 6.9
10 5.6
3
14 8.5
6 7.4
6 9.6
Output: Bank A
"""