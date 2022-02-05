class Solution:
	def strStr(self, haystack: str, needle: str) -> int:
		if needle == "" or needle == haystack:
			return 0
		h_len, n_len = len(haystack), len(needle)
		for i in range(0, h_len - n_len + 1):
			if haystack[i:i+n_len] == needle:
				return i
		return -1