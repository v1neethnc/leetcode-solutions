class Solution:
	def plusOne(self, digits: List[int]) -> List[int]:
		carry = 1
		for ind in range(len(digits) - 1, -1, -1):
			if carry == 0:
				break
			digits[ind] = digits[ind] + carry
			carry = digits[ind] // 10
			digits[ind] = digits[ind] % 10
		if carry != 0:
			tmp = [i for i in digits]
			digits[0] = carry
			digits[1:] = tmp
		return digits