class Solution:
	def lengthOfLongestSubstring(self, s: str) -> int:
		length, begin, end = 0, 0, 0
		characters = set()
		while end < len(s):
			if s[end] not in characters:
				characters.add(s[end])
				end += 1
				length = max(length, len(characters))
			else:
				characters.remove(s[begin])
				begin += 1
		return length