class Solution:
	def mergeAlternately(self, word1: str, word2: str) -> str:
		res = ''
		for i in range(0, max(len(word1), len(word2))):
			ch1 = word1[i] if i < len(word1) else ''
			ch2 = word2[i] if i < len(word2) else ''
			res = res + ch1 + ch2
		return res