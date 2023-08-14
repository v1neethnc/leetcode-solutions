class Solution:
	def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
		res_dict = {}
		res_counts = [0 for i in range(k)]
		for log in logs:
			if log[0] in res_dict:
				res_dict[log[0]].add(log[1])
			else:
				res_dict[log[0]] = set([log[1]])
		res_vals = {i: len(res_dict[i]) for i in res_dict.keys()}
		for i in res_vals.values():
			res_counts[i-1] += 1
		return res_counts