import sys

fileIN = open(sys.argv[1], "r")
pattern = sys.argv[2]
line = fileIN.readline()
   
while line:
    if line[:2] == "@@":
        break
    else:
        if line.find(pattern) != -1:
            print "found it!"
            break

    line = fileIN.readline()

