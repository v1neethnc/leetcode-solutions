class Solution:
	def replaceDigits(self, s: str) -> str:
		res = ''
		for ind in range(1, len(s), 2):
			res += s[ind - 1] + chr(ord(s[ind - 1]) + int(s[ind]))
		if len(res) < len(s):
			res += s[len(res):]
		return res