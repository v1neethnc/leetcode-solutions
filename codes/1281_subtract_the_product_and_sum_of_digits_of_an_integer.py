class Solution:
	def subtractProductAndSum(self, n: int) -> int:
		sm, prd = 0, 1
		while n > 0:
			vl = n % 10
			sm += vl
			prd *= vl
			n = n//10
		return prd - sm