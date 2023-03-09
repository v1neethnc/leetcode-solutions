class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        ctr_map = {i:[] for i in set(groupSizes)}
        for ind, val in enumerate(groupSizes):
            ctr_map[val].append(ind)
        res = []
        for key in ctr_map.keys():
            set_counts = len(ctr_map[key]) // key
            for i in range(set_counts):
                res.append(ctr_map[key][i*key:(i+1)*key])
        return res