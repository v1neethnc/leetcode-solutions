class Solution:
	def isPalindrome(self, x: int) -> bool:
		nm = str(x)
		return nm == nm[::-1]