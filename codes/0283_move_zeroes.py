class Solution:
	def moveZeroes(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		ln, tmp = len(nums), [i for i in nums if i != 0]
		nums[0:] = tmp
		nums[len(nums):] = [0 for i in range(0, ln - len(nums))]