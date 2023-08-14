class Solution:
	def multiply(self, num1: str, num2: str) -> str:
		val1, val2 = 0, 0
		for i in num1:
			val1 = val1 * 10 + int(i)
		for i in num2:
			val2 = val2 * 10 + int(i)
		return str(val1 * val2)