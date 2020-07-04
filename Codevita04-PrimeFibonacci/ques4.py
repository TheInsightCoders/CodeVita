def prime(n):
 flag = 0
 for i in range(2,int(n**0.5)+1):
  if n%i==0:
   flag = 1
   break
 return flag

n,m =input().split()
n=int(n)
m=int(m)
Prime1=[]

for i in range(n,m+1):
 if prime(i)==0:
  Prime1.append(i)

Prime2=[]

for i in Prime1:
 for j in Prime1:
  cross_prod = int(str(i)+str(j))
  if prime(cross_prod)==0 and cross_prod not in Prime2:
   Prime2.append(cross_prod)

num1=min(Prime2)
num2=max(Prime2)

for i in range(len(Prime2)-2):
 sum=num1+num2
 num1=num2
 num2=sum
print(sum,end="")