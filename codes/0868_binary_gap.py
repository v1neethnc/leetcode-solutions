class Solution:
	def binaryGap(self, n: int) -> int:
		start, nxt, dist = 0, 1, 0
		st = bin(n)
		st = st[2:]
		while nxt < len(st):
			if st[start] != '1':
				start += 1
				continue
			if st[nxt] == '1':
				dist = max(dist, nxt - start)
				start = nxt
			nxt += 1
		return dist