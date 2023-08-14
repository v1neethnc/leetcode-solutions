class Solution:
	def isAnagram(self, s: str, t: str) -> bool:
		letters = set(s)
		letters = letters.union(set(t))
		for i in letters:
			if s.count(i) != t.count(i):
				return False
		return True