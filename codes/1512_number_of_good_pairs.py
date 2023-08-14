class Solution:
	def numIdenticalPairs(self, nums: List[int]) -> int:
		visited = []
		ctr = 0
		for i in nums:
			if i not in visited and nums.count(i) > 1:
				nm_ctr = nums.count(i)
				ctr += (nm_ctr * (nm_ctr - 1) // 2)
				visited.append(i)
		return ctr