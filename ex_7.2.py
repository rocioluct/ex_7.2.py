 Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
suma = 0
for line in fh:
    line = line.rstrip()
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    posdospun = line.find(":")
    posnum =  line[posdospun + 2:]
    fposnum= float(posnum)
    suma = suma + fposnum
    count = count + 1
print ("Average spam confidence: ", suma/count)
