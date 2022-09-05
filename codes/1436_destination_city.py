class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, dests = set([i[0] for i in paths]), set([i[1] for i in paths])
        return list(dests - starts)[0]