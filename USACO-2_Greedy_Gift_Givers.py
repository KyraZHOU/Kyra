fin = open('gift1.in','r')
fout = open('gift1.out','w')

#Determine the number of people
NP = int(fin.readline())

#Check the length name of each people
def CheckLen(name):
	'''Check the length of the name'''
	if 0< len(name) <= 14:
		CheckLen = True
	else:
		CheckLen = False
	return CheckLen

#Initialise a list called name to store names
name = []

#Append names into the list called name
for i in range(NP):
	name.append(fin.readline())
	for i in name:
		if CheckLen(i) == False:
			print("No one of whom has a name longer than 14 characters.")
			break
		else:
			pass

#Determine the total number of stopLines in a file
with open('gift1.in') as f:
	size = len(f.readlines())
	print(size)

#set lists to determine the money each one got
money = [0]*NP
print(money)

#
stopLine = 0

while stopLine < size - NP:
	#determine the people who gives out
	personGiven = fin.readline()
	stopLine += 1
	for i in range(NP):
		if name[i] == personGiven:
			monGiven = fin.readline().split()
			stopLine += 1
			totalGiven = int(monGiven[0])
			peopleGiven = int(monGiven[1])
			if peopleGiven == 0:
				break
			money[i] = money[i] - peopleGiven * int(totalGiven/peopleGiven)
			for k in range(peopleGiven):
				peopleRecv = fin.readline()
				stopLine += 1
				RecvInd = -1
				while RecvInd < NP-1:
					RecvInd += 1
					if peopleRecv == name[RecvInd]:
						money[RecvInd] = money[RecvInd] + int(totalGiven/peopleGiven)
print(money)
for i in range(NP):
	name[i] = name[i].strip('\n')
for i in range(NP):
	fout.write(str(name[i])+' '+str(money[i])+'\n')
