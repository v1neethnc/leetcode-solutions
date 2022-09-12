class Solution:
	def runningSum(self, nums: List[int]) -> List[int]:
		res, prev = [], 0
		for i in nums:
			res.append(prev + i)
			prev = prev + i
		return res