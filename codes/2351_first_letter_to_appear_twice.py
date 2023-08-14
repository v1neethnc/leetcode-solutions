class Solution:
	def repeatedCharacter(self, s: str) -> str:
		chars = set()
		for i in s:
			if i in chars:
				return i
			chars.add(i)