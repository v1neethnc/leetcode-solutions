class Solution:
	def isValid(self, s: str) -> bool:
		open_brackets = []
		bracket_pairs = {')': '(', ']':'[', '}':'{'}        
		for i in s:
			if i in "([{":
				open_brackets.append(i)
			elif len(open_brackets) == 0:
				return False
			elif open_brackets[-1] != bracket_pairs[i]:
				return False
			else:
				open_brackets = open_brackets[:-1]
		if len(open_brackets) > 0:
			return False
		return True