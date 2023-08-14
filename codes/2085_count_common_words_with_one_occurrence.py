class Solution:
	def countWords(self, words1: List[str], words2: List[str]) -> int:
		intersection_set = list(set(words1).intersection(words2))
		ctr = 0
		for i in intersection_set:
			if words1.count(i) == 1 and words2.count(i) == 1:
				ctr += 1
		return ctr