'''
1
6
3 6 5 4 1 2
'''
t=int(input())
x=[]
for j in range(t):
    count=0
    n=int(input())
    x=list(map(int,input().split()))
    x.insert(0,0)
    y=list(range(n+1))
    ori_pos = y
    while True:
        z=[0]*(n+1)
        for i in range(1,n+1):
            z[x[i]]=y[i]
        count+=1
        if z == ori_pos:
            print(count, end ='')
            break
        else:
            y = z