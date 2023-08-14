class Solution:
    def myAtoi(self, s: str) -> int:
        if len(s) == 0:
            return 0
        sign = 1
        s = s.lstrip()
        ind = 0
        num = 0
        isdecimal = False
        issign = False
        while ind < len(s) and not s[ind].isdigit():
            print(ind)
            if s[ind] not in '+-.':
                return 0
            if s[ind] == '.':
                isdecimal = True
            if s[ind] in '+-':
                if issign:
                    return 0
                sign = -1 if s[ind] == '-' else 1
                issign = True
            ind += 1
        if ind == len(s):
            return 0
        s = s[ind:]
        ind = 0
        if isdecimal:
            return 0
        while ind < len(s) and s[ind].isdigit():
            num = num*10 + int(s[ind])
            ind += 1
        if isdecimal:
            num = num / 10**ind        
        num *= sign
        if num < -2**31:
            return -2**31
        if num >= 2**31:
            return 2**31-1
        return (num)