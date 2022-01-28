class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		index_map = {}
		for ind, num in enumerate(nums):
			diff = target - num
			if diff in index_map.keys():
				return [ind, index_map[diff]]
			else:a
				index_map[num] = ind