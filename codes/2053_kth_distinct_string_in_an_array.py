class Solution:
	def kthDistinct(self, arr: List[str], k: int) -> str:
		res = [i for i in arr if arr.count(i) == 1]
		return res[k-1] if len(res) >= k else ""