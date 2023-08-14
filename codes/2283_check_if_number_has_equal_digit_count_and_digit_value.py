class Solution:
	def digitCount(self, num: str) -> bool:
		for ind in range(len(num)):
			if num.count(str(ind)) != int(num[ind]):
				return False
		return True