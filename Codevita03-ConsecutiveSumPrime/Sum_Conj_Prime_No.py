n = int(input())
arr = []
count = 0

primes = [i for i in range(2,n+1) if all(i%j !=0 for j in range(2,int(i**0.5) + 1))]


for i in range(2, len(primes)):
    sum = 0
    for j in primes:
        sum += j
        if sum == primes[i]:
            count +=1
            break
        if sum > primes[i]:
            break
print(count)