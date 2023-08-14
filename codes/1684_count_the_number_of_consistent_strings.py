class Solution:
	def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
		ctr = 0
		st_allowed = set(allowed)
		for i in words:
			if set(i).issubset(st_allowed):
				ctr += 1
		return ctr