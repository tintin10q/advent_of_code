while True:
	lijst = input("Input:")
	lijst = list(lijst)
	totaal = 0
	check1 = 0
	check2 = 0
	for i in lijst:
		check2 = i
		#print(check1,check2)
		if check1 == check2:
			totaal+= int(check2)
			
		check1 = check2
	if lijst[0] == lijst[len(lijst)-1]:
		totaal += int(lijst[len(lijst)-1])
	print(totaal)
	
#sla op 
#combineer check met de vorige
#als goed tel op
#schuif door