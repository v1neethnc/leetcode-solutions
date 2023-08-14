class Solution:
	def findNumbers(self, nums: List[int]) -> int:
		ctr = 0
		for i in nums:
			if len(str(i)) % 2 == 0:
				ctr += 1
		return ctr