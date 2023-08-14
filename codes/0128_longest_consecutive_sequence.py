class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))
        nums.sort()
        max_len, prev = 0, None
        for val in nums:
            if prev == None or prev != val - 1:
                len_val = 1
            elif prev == val - 1:
                len_val += 1
            prev = val
            max_len = max(max_len, len_val)
        return max_len