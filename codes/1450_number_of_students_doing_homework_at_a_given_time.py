class Solution:
	def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
		ctr = 0
		for i in range(len(endTime)):
			if endTime[i] >= queryTime:
				if startTime[i] <= queryTime:
					ctr += 1
		return ctr