class Solution:
    def longestContinuousSubstring(self, s: str) -> int:
        main_string = 'abcdefghijklmnopqrstuvwxyz'
        start, end = 0, 1
        max_len = 0
        while start < len(s):
            if end > len(s):
                start += 1
                continue
            if s[start:end] in main_string:
                # print(start, end, s[start:end], max_len, end-start)
                max_len = max(max_len, end - start)
                end += 1
            else:
                start += 1
                end = start + 1
        return max_len