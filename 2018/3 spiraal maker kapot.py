from math import sqrt
'''
37-36-35-34-33-32-31
38-17-16-15-14-13-30
39-18-5--4--3--12-29
40-19-6--1--2--11-28
41-20-7--8--9--10-27
42-21-22-23-24-25-26
43-44-45-46-47-48-49-50
'''
# first corners [10,13,17,21,26,31,37,43,50]


'''
start bij 1
waarschijnlijk in 414 blijkbaar 323
per circle zijn er circleVorige*4+4 cijvers
de lengte van elke circel zijde is vorigecircel+2
elke corner een teken invoegen van dat je een corner maakt en dat
teken geeft dan de goede richting aans
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
		print(self.coordinate,currentNumber)
		if currentNumber == self.target: # Set up output
			print("done!")
			self.total = 0
			for i in self.coordinate:
				self.total += sqrt(i**2)
			print(self.total)
	
def rightUp(lijstInput,iInput):
	global id
	id += 1
	lijstInput.append(iInput)
	lijstInput.append("<<<") #+str(id)
	return lijstInput
	
def rightDown(lijstInput,iInput):
	global id
	id += 1
	lijstInput.append(iInput)
	lijstInput.append("^^^")
	return lijstInput	
	
def leftUp(lijstInput,iInput):
	global id
	id += 1
	lijstInput.append(iInput)
	lijstInput.append("VVV")
	return lijstInput	
	
def leftDown(lijstInput,iInput):
	global id
	id += 1
	lijstInput.append(iInput)
	lijstInput.append(">>>")
	return lijstInput

while True:
	puzzleInput = int(input("puzzleInput:")) # Mine is 347991
	lijstLimit = puzzleInput + 2
	lijst = [1,2,"^^^",3,"<<<",4,5,"VVV",6,7,">>>",8]
	circleID = 0
	conersToDo = 0
	skip = 3
	skipCounter = 2
	skipPlus = 1
	i = 9
	id = 4

	limiet = 1
	circleLimiet = 500 #int(input("CircleLimiet:"))
	
	while i < lijstLimit: #or circleID < circleLimiet: But only if you know where your puzzleInput is so first is better 
		skipCounter += 1
		if skipCounter == skip:
			if conersToDo == 1:
				lijst = leftDown(lijst,i)
				i += 1
			elif conersToDo == 2:
				lijst = leftUp(lijst,i)
				i += 1
			elif conersToDo == 3:
				lijst = rightUp(lijst,i)
				i += 1
			skipCounter = 0
			if conersToDo == 0:
				skip += skipPlus
				conersToDo = 4
				skipCounter = skipPlus-1
				skipPlus += 1
				lijst.append(i)
				i += 1
				lijst = rightDown(lijst,i)
				i += 1
				circleID += 1
				#print(circleID)
			conersToDo -= 1
		else:
			lijst.append(i)
			i += 1
		if i == 11:
			skipCounter +=1
		#print("skip:",skip," skipCounter:",skipCounter," skipPlus:",skipPlus," conersToDo:",conersToDo," i:",i," circleID:",circleID,sep="")
	'''
	with open('File path', 'w') as f:
		f.write(str(lijst))
		f.write("\n")
		f.write("Last CircleID: ")
		f.write(str(circleID))
		f.close()
	'''
	#rember dat mode change met >>> moet
	print(lijst)
	walker = runningMan(puzzleInput)
	for i in lijst:
		walker.runForward(i)
		if i == puzzleInput:
			break













