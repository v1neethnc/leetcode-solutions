class Solution:
	def halvesAreAlike(self, s: str) -> bool:
		ctr = {'vowels': 0, 'consonants': 0}
		for i in s[:len(s)//2]:
			if i in 'aeiouAEIOU':
				ctr['vowels'] += 1
			else:
				ctr['consonants'] += 1
		for i in s[len(s)//2:]:
			if i in 'aeiouAEIOU':
				ctr['vowels'] -= 1
			else:
				ctr['consonants'] -= 1
		return True if ctr['vowels'] == 0 and ctr['consonants'] == 0 else False