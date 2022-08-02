class Solution:
	def firstUniqChar(self, s: str) -> int:
		if len(s) == 1:
			return 0
		for i in range(0, len(s) - 1):
			if s[i] not in s[i+1:] and s[i] not in s[:i]:
				return i
		if s.count(s[-1]) == 1:
			return s.index(s[-1])
		return -1