n = int(input())

list1 = []
for i in range(1,int(n**0.5)+1):
	if n%i == 0:
		if i*i == n:
			print(i,end = " ")
		else:
			print(i,end = " ")
			list1.insert(0,n//i)

for i in list1:
	print(i,end = " ")