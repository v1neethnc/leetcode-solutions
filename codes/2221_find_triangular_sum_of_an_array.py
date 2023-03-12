class Solution:
	def triangularSum(self, nums: List[int]) -> int:
		while len(nums) > 1:
			tmp_list = []
			for ind in range(len(nums) - 1):
				tmp_list.append((nums[ind] + nums[ind + 1]) % 10)
			nums = [i for i in tmp_list]
		return nums[0]