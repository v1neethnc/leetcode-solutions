class Solution:
	def complexNumberMultiply(self, num1: str, num2: str) -> str:
		n1, n2 = num1.split('+'), num2.split('+')
		coeff1 = int(n1[0]) * int(n2[0]) - int(n1[1][:-1]) * int(n2[1][:-1])
		coeff2 = int(n1[0]) * int(n2[1][:-1]) + int(n1[1][:-1]) * int(n2[0])
		return str(coeff1) + '+' + str(coeff2) + 'i'