from math import sqrt
class runningMan():
	def __init__(self,target):
		self.mode = ">>>"
		self.target = target
		self.coordinate = [0,0]
		print("starting walkingman met target:",self.target)
	def changeMode(self,modeInput):
		if modeInput in (">>>","<<<","^^^","VVV"):
			self.mode = modeInput
	def runForward(self,currentNumber):
		if currentNumber not in (">>>","<<<","^^^","VVV"): # Als het dus niet een mode changer is
			if self.mode == ">>>":
				self.coordinate[0] += 1
			elif self.mode == "<<<":
				self.coordinate[0] -= 1
			elif self.mode == "^^^":
				self.coordinate[1] += 1
			elif self.mode == "VVV":
				self.coordinate[1] -= 1
			if currentNumber == 1: # Dit is omdat op plek 1 de afstand 0 is en niet 1 en zo maak je die uitzondering 
				self.coordinate = [0,0]
		else: # Als het wel een mode changer is dan veranderd de mode
			self.changeMode(currentNumber)
		print(self.coordinate,currentNumber)
		if currentNumber == self.target: # Set up output
			print("done!")
			self.total = 0
			for i in self.coordinate:
				self.total += sqrt(i**2)
			print(self.total)

while True:
	puzzleInput = int(input("Target:"))
	lijst = [1, 2, '^^^', 3, '<<<', 4, 5, 'VVV', 6, 7, '>>>', 8, 9, 10, '^^^', 11, 12, 13, '<<<', 14, 15, 16, 17, 'VVV', 18, 19, 20, 21, '>>>', 22, 23, 24, 25, 26, '^^^', 27, 28, 29, 30, 31, '<<<',32,33,34,35,36,37]
	walker = runningMan(puzzleInput)
	for i in lijst:
		walker.runForward(i)
		if i == puzzleInput:
			break
		
