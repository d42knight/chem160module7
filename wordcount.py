import sys
from collections import Counter
from os import path
filename=input("Enter the name of the file")
if not os.path.exists(filename):
    sys.exit("Cannot find file given")
file=open(filename,"r")
words=[]
while 1:
    line=file.readline()
    if line=="":
        break
    words.extend(line.split())
counts=Counter(words)
for i in countrs:
    print("%2d: %s"%(counts[i],i))
