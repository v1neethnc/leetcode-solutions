class Solution:
	def singleNumber(self, nums: List[int]) -> int:
		nums_set = set(nums)
		for i in nums_set:
			if nums.count(i) == 1:
				return i