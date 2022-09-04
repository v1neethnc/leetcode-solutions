class Solution:
	def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
		counter = [0 for i in range(102)]
		for i in nums:
			counter[i+1] += 1
		for i in range(1,len(counter)):
			counter[i] += counter[i-1]
		return [counter[i] for i in nums]