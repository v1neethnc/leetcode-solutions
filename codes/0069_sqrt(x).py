class Solution:
	def mySqrt(self, x: int) -> int:
		i = 1
		while i < x//i:
			i += 1
		return i if i*i <= x else i - 1