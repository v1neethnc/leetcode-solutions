class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        indices_list = {i: [] for i in range(0, numRows)}
        temp_val = 0
        direction = 1
        for letter in s:
            indices_list[temp_val].append(letter)
            if temp_val == 0:
                direction = 1
            if temp_val == numRows - 1:
                direction = -1
            temp_val += direction
        return ''.join([''.join(indices_list[key]) for key in indices_list])