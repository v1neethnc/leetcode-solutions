class Solution:
	def areOccurrencesEqual(self, s: str) -> bool:
		ctr = {i: s.count(i) for i in set(s)}
		return len(set(list(ctr.values()))) == 1