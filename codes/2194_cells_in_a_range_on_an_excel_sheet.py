class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        limits = s.split(':')
        res = [chr(i) + str(j) for i in range(ord(limits[0][0]), ord(limits[1][0]) + 1) for j in range(int(limits[0][1]), int(limits[1][1]) + 1)]
        return res