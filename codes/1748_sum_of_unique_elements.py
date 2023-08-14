class Solution:
	def sumOfUnique(self, nums: List[int]) -> int:
		num_dict = {}
		for i in nums:
			if i in num_dict:
				num_dict[i] += 1
			else:
				num_dict[i] = 1
		return sum([i for i in num_dict.keys() if num_dict[i] == 1])