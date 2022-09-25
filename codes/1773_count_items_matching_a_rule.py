class Solution:
	def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
		index_map = {"type": 0, "color": 1, "name": 2}
		ctr = 0
		for i in items:
			if i[index_map[ruleKey]] == ruleValue:
				ctr += 1
		return ctr