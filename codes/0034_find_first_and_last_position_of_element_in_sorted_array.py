class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]
        return [nums.index(target), nums.index(target) + nums.count(target) - 1]