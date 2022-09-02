class Solution:
	def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
		new_grid = []
		res = 0
		for r_ind in range(0, len(grid)):
			m1 = max(grid[r_ind])
			for c_ind in range(0, len(grid[r_ind])):
				res += (min(m1, max([i[c_ind] for i in grid])) - grid[r_ind][c_ind])
		return res