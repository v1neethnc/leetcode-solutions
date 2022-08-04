class Solution:
	def convertToBase7(self, num: int) -> str:
		res = ''
		if num == 0:
			return "0"
		flag = False if num >= 0 else True
		num = abs(num)
		while num > 0:
			res = str(num % 7) + res
			num = num // 7
		if flag:
			res = '-' + res
		return res