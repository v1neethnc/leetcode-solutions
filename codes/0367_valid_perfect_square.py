class Solution:
	def isPerfectSquare(self, num: int) -> bool:
		return str(num**0.5)[-2:] == '.0'