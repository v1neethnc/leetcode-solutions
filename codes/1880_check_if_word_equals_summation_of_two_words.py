class Solution:
	def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
		f_val = int(''.join([str(ord(i) - ord('a')) for i in firstWord]))
		s_val = int(''.join([str(ord(i) - ord('a')) for i in secondWord]))
		t_val = int(''.join([str(ord(i) - ord('a')) for i in targetWord]))
		return f_val + s_val == t_val