class Solution:
	def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
		res = [min(i) for i in rectangles]
		return res.count(max(res))