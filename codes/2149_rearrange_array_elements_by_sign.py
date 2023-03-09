class Solution:
	def rearrangeArray(self, nums: List[int]) -> List[int]:
		pos_nums, neg_nums = [i for i in nums if i > 0], [i for i in nums if i < 0]
		res = []
		for i in range(len(pos_nums)):
			res.append(pos_nums[i])
			res.append(neg_nums[i])
		return res