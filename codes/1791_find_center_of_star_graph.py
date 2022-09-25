class Solution:
	def findCenter(self, edges: List[List[int]]) -> int:
		hashmap = dict()
		for i in edges:
			for j in i:
				if j in hashmap.keys():
					hashmap[j] += 1
				else:
					hashmap[j] = 1
		vl = len(hashmap.keys())
		for i in hashmap.keys():
			if hashmap[i] == vl - 1:
				return i