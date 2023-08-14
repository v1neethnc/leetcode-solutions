class Solution:
    def reverse(self, x: int) -> int:
        vl = str(x)
        if vl[0] == '-':
            res = '-' + vl[-1:-len(vl):-1]
        else:
            res = vl[::-1]
        res = int(res)
        if res not in range(-2147483648, 2147483648):
            return 0
        return res