class Solution:
	def heightChecker(self, heights: List[int]) -> int:
		sorted_heights = [i for i in heights]
		sorted_heights.sort()
		ctr = 0
		for i in range(0, len(sorted_heights)):
			if heights[i] != sorted_heights[i]:
				ctr += 1
		return ctr