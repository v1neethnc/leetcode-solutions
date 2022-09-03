class Solution:
	def freqAlphabets(self, s: str) -> str:
		ind = 0
		res = ''
		while ind < len(s):
			if ind + 2 < len(s) and s[ind + 2] == '#':
				res += chr(ord('a') + int(s[ind: ind+ 2]) - 1)
				ind += 3
			else:
				res += chr(ord('a') + int(s[ind]) - 1)
				ind += 1
		return res