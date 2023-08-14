class Solution:
	def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
		res = [-1 for i in range(len(nums))]
		for i in range(len(nums)):
			if res[index[i]] == -1:
				res[index[i]] = nums[i]
			else:
				tmp = [j for j in res[:index[i]]]
				tmp.append(nums[i])
				res = tmp + res[index[i]: len(nums)]
		res = [res[i] for i in range(len(nums))]
		return res