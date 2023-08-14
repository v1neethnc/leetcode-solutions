class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        nums = ''
        list_nums = []
        for char in s:
            if char.isdigit():
                nums += char
            else:
                if len(nums) > 0:
                    list_nums.append(int(nums))
                nums = ''
        if len(nums) > 0:
            list_nums.append(int(nums))
        
        for i in range(1, len(list_nums)):
            if list_nums[i-1] >= list_nums[i]:
                return False
        return True
