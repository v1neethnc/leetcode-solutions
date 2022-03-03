class Solution:
	def countPrimes(self, n: int) -> int:
		if n == 0 or n == 1:
			return 0
		n = n - 1
		prime = [True for i in range(n+1)] 
		p = 2
		while (p * p <= n): 
			if (prime[p] == True): 
				for i in range(p * p, n+1, p): 
					prime[i] = False
			p += 1
		prime[0], prime[1] = False, False
		return prime.count(True)