#### Generation of Prime Numbers List ####

########################## First #############################
# Python program to print all
# prime number in an interval

start = 2
end = 20

for val in range(2,20):                      #(start,end+1)
	#  If num is divisible by any number
	# between 2 and val, it is not prime
	if val > 1:
		for n in range(2, val):
			if (val % n) == 0:
				break
		else:
			print(val)


########################## Second #############################
primes = [i for i in range(2,20) if all(i%j !=0 for j in range(2,int(i**0.5) + 1))]
print(primes)

non_primes = [ i for i in range(2,20) if any(i%j == 0 for j in range(2, int(i**0.5)+1))]
print(non_primes)

print(set(primes).union(set(non_primes)))

########################## Third #############################
# below list contains prime and non-prime in range 1 to 50
noprimes = [j for i in range(2, 8) for j in range(i*2, 50, i)]
primes = [x for x in range(2, 50) if x not in noprimes]
print( primes )
print( noprimes )