class Solution:
	def targetIndices(self, nums: List[int], target: int) -> List[int]:
		nums.sort()
		return [] if target not in nums else [i for i in range(nums.index(target), nums.index(target) + nums.count(target))]