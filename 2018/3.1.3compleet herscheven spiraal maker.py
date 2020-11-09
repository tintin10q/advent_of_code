from math import sqrt
'''
37-36-35-34-33-32-31
38-17-16-15-14-13-30
39-18-5--4--3--12-29
40-19-6--1--2--11-28
41-20-7--8--9--10-27
42-21-22-23-24-25-26
43-44-45-46-47-48-49-50

start bij 1
elke corner een teken invoegen van dat je een corner maakt en dat
teken geeft dan de goede richting aans

	
voeg toe aan lijst
als corner value (wanneer de normaalcount dezelfde waarde heeft als normaal):
	voeg turn in
	keep track of welke corner je bent zodat je goede turn invoegt en zodat je speciale corners kan doen 
ls specaal corner value:
	ga 1 exstra vooruit en voeg turn in
	ga dan 1 minder 
	en dan weer 1 meer 
	
'''

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
		if currentNumber == self.target: # Set up output
			self.total = 0
			for i in self.coordinate:
				self.total += sqrt(i**2)
			print("De afstand is:",self.total)
	
def rightUp(lijstInput):
	global id
	id += 1
	lijstInput.append("<<<") #+str(id)
	return lijstInput
	
def rightDown(lijstInput):
	global id
	id += 1
	lijstInput.append("^^^")
	return lijstInput	
	
def leftUp(lijstInput):
	global id
	id += 1
	lijstInput.append("VVV")
	return lijstInput	
	
def leftDown(lijstInput):
	global id
	id += 1
	lijstInput.append(">>>")
	return lijstInput

while True:
	puzzleInput = int(input("puzzleInput:")) # Mine is 347991
	id = 0
	i = 3
	lijst = [1,2,"^^^"]
	start = 1
	normaalCounter = 0
	normaal = 1
	corner = 1
	
	while i < puzzleInput+1:
		lijst.append(i)
		normaalCounter += 1
		if normaal == normaalCounter:
			if corner == 3:
				normaal += 1
				normaalCounter = 0
				lijst = leftDown(lijst)
				corner = 0
			elif corner == 2:
				corner += 1
				normaalCounter = 0
				lijst = leftUp(lijst)
			elif corner == 1:
				normaal = normaal + 1
				normaalCounter = 0
				corner += 1
				lijst = rightUp(lijst)
			elif corner == 0:
				lijst = rightDown(lijst)
				corner += 1
				normaalCounter = 0
		i += 1

	walker = runningMan(puzzleInput)
	for i in lijst:
		walker.runForward(i)
		if i == puzzleInput:
			break













