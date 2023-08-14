class Solution:
	def addStrings(self, num1: str, num2: str) -> str:
		v1, v2, carry = 0, 0, 0
		ln = max(len(num1), len(num2))
		res = ''
		for i in range(1, ln+1):
			# print(v1, v2, res, carry)
			v1 = int(num1[-i]) if i < len(num1) + 1 else 0
			v2 = int(num2[-i]) if i < len(num2) + 1 else 0
			res = str((v1 + v2 + carry) % 10) + res
			carry = (v1 + v2 + carry) // 10
		if carry != 0:
			res = str(carry) + res
		return res