class Solution:
	def arrangeCoins(self, n: int) -> int:
		return (int) ((n * 8 + 1) ** 0.5 - 1) // 2