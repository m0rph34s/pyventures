# Kandinsky
# The Sieve of Eratosthenes!

def sieve(n):
	
	# 1.Create a list of consecutive integers from 2 through n: (2, 3, 4, ..., n).
	l=list(range(2, n + 1))
	#l = [x for x in range(2, n + 1) if not x % 2 == 0]
	print("List of all numbers up to limit: ", l, '\n')
	
	# 2.Initially, let p equal 2, the smallest prime number.
	p = 2 

	# 3.Enumerate the multiples of p by counting to n from 2p in increments of p, and mark them in the list (these will be 2p, 3p, 4p, ...; the p itself should not be marked).
	not_prime = [] # this will be populated with non-prime integers
	
	xp = 4
	
	for num in l:
		p = num
		# keep enumerating multiples xp until xp exceeds the upper limit n
		#print("Galina what the fuck")
		for i in range(p, int(((n+1)/num))+ 1):
			xp = p * i
			#print("p value: ", p, "xp value: ", xp)
			if xp > n:
				#print("Breaking")
				break
			if xp not in not_prime:
				not_prime.append(xp)

		#print("Found non-primes so far: ", not_prime)
		# 4.Find the first number greater than p in the list that is not marked. If there was no such number, stop. 
		#  		Otherwise, let p now equal this new number (which is the next prime), and repeat from step 3.
		# remove all the non-primes from the list to examine, l, and loop back!
		l = [x for x in l if x not in not_prime]

	# 5.When the algorithm terminates, the numbers remaining not marked in the list are all the primes below n.
	print("The prime numbers up to %s are: "%(n),l)

sieve(int(input("Welcome to the Sieve of Eratosthenes.\nProvide the limit up to which you wish to find the prime numbers, must be > 2: ")))