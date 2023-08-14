class Solution:
	def xorOperation(self, n: int, start: int) -> int:
		res = 0
		for i in range(0, n):
			res ^= (start + i * 2)
		return res