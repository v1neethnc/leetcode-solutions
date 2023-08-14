class Solution:
	def replaceElements(self, arr: List[int]) -> List[int]:
		return [max(arr[i+1:]) if i != len(arr) - 1 else -1 for i in range(0, len(arr))]