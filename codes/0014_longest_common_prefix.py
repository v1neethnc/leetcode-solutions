class Solution:
	def longestCommonPrefix(self, strs: List[str]) -> str:
		ind, min_len, res = 0, len(strs[0]), ""
		for i in strs:
			min_len = min(min_len, len(i))
		for i in range(min_len):
			char = strs[0][i]
			for j in range(0, len(strs)):
				if strs[j][i] != char:
					return res
			res += char
		return res