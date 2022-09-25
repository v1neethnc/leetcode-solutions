class Solution:
	def squareIsWhite(self, coordinates: str) -> bool:
		col_val = ord(coordinates[0]) - ord('a')
		row_val = int(coordinates[1])
		return (col_val + row_val) % 2 == 0