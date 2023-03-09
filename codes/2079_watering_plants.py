class Solution:
	def wateringPlants(self, plants: List[int], capacity: int) -> int:
		steps = 0
		tmp_capacity = capacity
		for ind in range(len(plants)):
			if tmp_capacity >= plants[ind]:
				steps += 1
				tmp_capacity -= plants[ind]
			else:
				steps = steps + (2 * ind) + 1
				tmp_capacity = capacity - plants[ind]
		return steps