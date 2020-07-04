number = int(input())


five = int((number-4)/5)

if((number-5*five) % 2) == 0:
	one=2
else:
	one=1

two=(number-5*five-one)//2


print(one+two+five,five,two,one)
