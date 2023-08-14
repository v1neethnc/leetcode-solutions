class Solution:
	def titleToNumber(self, columnTitle: str) -> int:
		exp, res = 0, 0
		for i in columnTitle[::-1]:
			res = res + ((ord(i) - ord('A') + 1) * (26**exp))
			exp += 1
		return ress