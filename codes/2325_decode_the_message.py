class Solution:
	def decodeMessage(self, key: str, message: str) -> str:
		key_dict = {}
		letter_val = ord('a')
		for i in key:
			if i not in key_dict and i != ' ':
				key_dict[i] = chr(letter_val)
				letter_val += 1
		res = ''
		for i in message:
			to_append = ' '
			if i != ' ':
				to_append = key_dict[i]
			res = res + to_append
		return res