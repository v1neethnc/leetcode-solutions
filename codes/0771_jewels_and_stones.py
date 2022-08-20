class Solution:
	def numJewelsInStones(self, jewels: str, stones: str) -> int:
		ctr = 0
		for i in jewels:
			ctr += stones.count(i)
		return ctr