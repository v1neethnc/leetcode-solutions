class Solution:
	def sortSentence(self, s: str) -> str:
		vals = [(i[:-1], i[-1]) for i in s.split(' ')]
		vals.sort(key = lambda x:x[1])
		return ' '.join([i[0] for i in vals])