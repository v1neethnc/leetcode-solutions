class Solution:
	def sumZero(self, n: int) -> List[int]:
		res = [i for i in range(-n//2 + 1, n//2 + 1)]
		if n%2 == 0:
			res.remove(0)
			res.append(-n//2)
		return res