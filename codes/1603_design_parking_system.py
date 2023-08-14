class ParkingSystem:

	def __init__(self, big: int, medium: int, small: int):
		self.lots = [big, medium, small]

	def addCar(self, carType: int) -> bool:
		if self.lots[carType - 1] > 0:
			self.lots[carType - 1] -= 1
			return True
		return False