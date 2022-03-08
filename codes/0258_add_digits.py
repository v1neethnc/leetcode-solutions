class Solution:
	def addDigits(self, num: int) -> int:
		sm = num
		while sm > 9:
			vals = [int(i) for i in str(sm)]
			sm = sum(vals)
		return sm