class Solution:
	def findWords(self, words: List[str]) -> List[str]:
		s1 = set("qwertyuiop")
		s2 = set("asdfghjkl")
		s3 = set("zxcvbnm")
		res = []
		for i in words:
			tmp = set(i.lower())
			if len(tmp) == len(tmp.intersection(s1)) or len(tmp) == len(tmp.intersection(s2)) or len(tmp) == len(tmp.intersection(s3)):
				res.append(i)
		return res