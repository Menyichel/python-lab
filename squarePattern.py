#square pattern using for loop by accepting #of rows andcolumns from the user
rc=int(input("\n Enter the number of rows and columns of square: "))
print ("\n-----The square pattern with "+ str(rc)+" rows and colums is-----\n")

for a in range(0,rc):
    for b in range(0,rc):
        print(end="# ")
    print(end="\n")
print("\n")
    
