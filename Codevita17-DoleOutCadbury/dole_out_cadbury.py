'''
5
7
3
4
'''


# LH  = int(input().strip())
# UH  = int(input().strip())
# LW  = int(input().strip())
# UW  = int(input().strip())
#
# dct = {}
# max_len = 0
# count = 0
#
# def f(x,y):
#   global count, max_len
#   count += 1
#   if x<y:
#     x, y = y,x
#   if x==0 or y==0:
#     return 0
#   if x==y:
#     return 1
#   else:
#     #return 1+f(x-y,y)
#     #'''
#     if (x,y) not in dct:
#       dct[(x,y)] = 1+f(x-y,y)
#       if len(dct)>max_len: max_len = len(dct)
#       if ((x-y,y) in dct): del dct[(x-y,y)]
#     return dct[(x,y)]
#     #'''
#
# res = 0
# for i in range(LH,UH+1):
#   for j in range(LW,UW+1):
#     res += f(i,j)
#
# print(res)


def count(a,b):
	minimum = min(a,b)
	maximum = max(a,b)

	i = (minimum,maximum)
	if i in D:
		return D[i]

	if minimum == 0:
		return 0
	if minimum == 1:
		return a*b

	chocolate = maximum // minimum
	new_side = maximum % minimum

	chocolate += count(new_side,minimum)

	D[i] = chocolate

	return chocolate

# Driver Code
D = {}
p  = int(input())
q  = int(input())
r  = int(input())
s  = int(input())

ans = 0

for i in range(p,q+1):
	for j in range(r,s+1):
		ans += count(i,j)

print(ans)