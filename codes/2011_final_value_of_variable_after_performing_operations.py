class Solution:
	def finalValueAfterOperations(self, operations: List[str]) -> int:
		val = 0
		for i in operations:
			val = val + 1 if i in ['X++', '++X'] else val - 1
		return val