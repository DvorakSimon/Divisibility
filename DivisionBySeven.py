"""
2022048
1946
"""
iNumberToCheck = 1946;
sNumberToCheck = str(iNumberToCheck);

while len(sNumberToCheck) != 2 and iNumberToCheck >= 0 and iNumberToCheck != 0:
	print(sNumberToCheck)
	prefix = sNumberToCheck[0:len(sNumberToCheck)-1]
	lastNumber = int(sNumberToCheck[len(sNumberToCheck)-1])
	sNumberToCheck = str(int(prefix) - (2*lastNumber))
	iNumberToCheck = int(sNumberToCheck)

if iNumberToCheck % 7 == 0:
	print("Number " + sNumberToCheck + " is dividible by 7!")

