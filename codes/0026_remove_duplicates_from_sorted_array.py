class Solution:
	def removeDuplicates(self, nums: List[int]) -> int:
		max_num = nums[-1] if len(nums) > 0 else 0
		ind = 0
		# print(nums)
		while ind < len(nums):
			counter = nums.count(nums[ind])
			if counter > 1:
				nums[ind + 1:] = nums[ind + counter:]
			# print(nums)
			ind += 1
		return len(nums)