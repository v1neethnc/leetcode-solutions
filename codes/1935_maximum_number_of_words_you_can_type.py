class Solution:
	def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
		words = text.split(' ')
		ctr = len(words)
		for i in words:
			for j in brokenLetters:
				if j in i:
					ctr -= 1
					break
		return ctr