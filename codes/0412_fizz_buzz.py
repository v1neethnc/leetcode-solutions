class Solution:
	def fizzBuzz(self, n: int) -> List[str]:
		result = []
		for i in range(0, n):
			if (i + 1) % 15 == 0:
				result.append('FizzBuzz')
			elif (i + 1) % 3 == 0:
				result.append('Fizz')
			elif (i + 1) % 5 == 0:
				result.append('Buzz')
			else:
				result.append(str(i + 1))
		return result