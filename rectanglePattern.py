#rectangle pattern by accepting #rows and #columns from the user
r = int (input ("Enter the number of rows: "))
c = int (input ("Enter the number of columns: "))

print ("\n-----The rectangle pattern with "+ str(r)+" rows and "+str(c)+" colums is-----\n")
for i in range (1, r+1):
	for j in range (1, c+1):
		if i == 1 or i == r or j == 1 or j == c:
			print (end="*  ")
		else:
			print(end="   ")

	print (end="\n\n")