while True:
	lijst = input("Input:")
	lijst = list(lijst)
	naarVoor = int(len(lijst)/2)
	#print("naar voor is:",naarVoor)
	totaal = 0
	check1 = 0
	check2 = 0
	plek = 0
	for i in lijst:
		check2 = i
		check1 = plek+naarVoor
		#print(check1)
		#print("lengte lijst:",len(lijst))
		if check1 >= len(lijst):
			check1 -= len(lijst)
		check1 = lijst[check1]
		#print(check1,check2,plek)
		if check1 == check2:
			totaal+= int(check2)
		plek += 1
	print(totaal)
	
#sla op 
#voor check 1 neem plek check2 en plus dat met de naarVoor als en dan - len(lijst) als het over len(lijst) gaat
#combineer check met de vorige
#als goed tel op
#schuif door