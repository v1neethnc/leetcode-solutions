class Solution:
	def maxPower(self, s: str) -> int:
		res = 1
		start, end = 0, 1
		while end < len(s):
			if s[start] == s[end]:
				res = max(res, end - start + 1)
				end += 1
			else:
				start += 1
				end = start + 1
		return res