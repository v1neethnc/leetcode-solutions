class Solution:
	def selfDividingNumbers(self, left: int, right: int) -> List[int]:
		res = []
		for i in range(left, right + 1):
			nms = [int(k) for k in str(i)]
			if 0 not in nms:
				flag = True
				for k in nms:
					if i % k != 0:
						flag = False
						break
				if flag:
					res.append(i)
		return res