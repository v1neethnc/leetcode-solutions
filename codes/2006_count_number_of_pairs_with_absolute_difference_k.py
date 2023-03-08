class Solution:
	def countKDifference(self, nums: List[int], k: int) -> int:
		ctr = 0
		for i in range(len(nums)-1):
			ctr += nums[i+1:].count(nums[i] + k) + nums[i+1:].count(nums[i] - k)
		return ctr