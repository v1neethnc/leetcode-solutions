class Solution:
	def hasGroupsSizeX(self, deck: List[int]) -> bool:
		ctrs = [deck.count(i) for i in set(deck)]
		print(ctrs)
		if 1 in ctrs:
			return False
		def gcd(a, b):
			while b:
				a, b = b, a%b
			return a
		gcd_val = ctrs[0]
		for i in range(1, len(ctrs)):
			gcd_val = gcd(gcd_val, ctrs[i])
		return True if gcd_val != 1 else False