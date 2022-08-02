class Solution:
	def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
		vals = [i for row in matrix for i in row]
		vals.sort()
		return vals[k-1]
