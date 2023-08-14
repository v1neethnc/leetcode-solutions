class Solution:
	def checkString(self, s: str) -> bool:
		ind = len(s) - 2
		prev = s[-1]
		while ind > -1:
			if ord(prev) - ord(s[ind]) < 0:
				return False
			prev = s[ind]
			ind -= 1
		return True