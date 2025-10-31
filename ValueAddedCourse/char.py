import os,sys

frame = input("Enter File Name: ")
if os.path.isfile(frame) :
    print("File Exists: ",frame)
    f = open(frame,"r")
else:
    print("File doesnt exist: ",frame)
    sys.exit(0)
lcount = wcount = ccount = 0

for line in f:
    lcount = lcount + 1
    ccount = ccount + len(line)
    words = line.split()
    wcount = wcount + len(words)

print("Lines: ",lcount)
print("Word Count: ",wcount)
print("Character Count: ",ccount)