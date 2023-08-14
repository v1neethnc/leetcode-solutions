class Solution:
	def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
		res = []
		for circle in queries:
			ctr = 0
			for coords in points:
				if (coords[0] - circle[0]) ** 2 + (coords[1] - circle[1]) ** 2 <= circle[2] ** 2:
					ctr += 1
			res.append(ctr)
		return res