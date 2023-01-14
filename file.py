# Python File 
# The open() function takes two parameters; filename, and mode("r,"a","w","x","t","b").

f = open("file.txt")
#print(f.read()) #read a file
# print(f.read(5))
print(f.readline())
f.close()

f = open("file.txt","a") # append the new content
f.write("Now the file has more content!")
f.close()

f = open("file.txt", "w")# "w" overwrite the whole document
f.write("This is overwritten content")
f.close()