class Solution:
	def missingNumber(self, nums: List[int]) -> int:
		if nums == [1]:
			return 0
		sum_of_list = sum(nums)
		nm = max(nums)
		val = (nm * (nm + 1) // 2) - sum_of_list
		return val if val > 0 else nm + 1 if 0 in nums else 0