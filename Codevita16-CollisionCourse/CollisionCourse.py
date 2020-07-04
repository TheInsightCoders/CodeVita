'''
5
5 12 1
16 63 5
-10 24 2
7 24 2
-24 7 2
'''

C = int(input())

D = {}
collision = 0

for i in range(C):
    x,y,speed=list(map(int,input().split()))

    sq_time=(x**2+y**2)/(speed**2)
    # print(sq_time)

    if(D.get(sq_time)==None):
        D[sq_time]=1
    else:
        D[sq_time]=D[sq_time]+1

# print(D)
for keys in D:
    if(D[keys]!=1):
        collision=collision+(D[keys]*(D[keys]-1))/2
print(int(collision))
