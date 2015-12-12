import sys

totalarea = 0
totalribbon = 0

for line in sys.stdin:
  dims = line.split('x')
  side1 = float(dims[0])*float(dims[1])
  side2 = float(dims[1])*float(dims[2])
  side3 = float(dims[0])*float(dims[2])
  totalarea += 2*side1+2*side2+2*side3
  totalarea += min(side1,side2,side3)
  volume = float(dims[0])*float(dims[1])*float(dims[2])
  perim1 = float(dims[0])*2 + float(dims[1])*2
  perim2 = float(dims[1])*2 + float(dims[2])*2
  perim3 = float(dims[0])*2 + float(dims[2])*2
  totalribbon += min(perim1,perim2,perim3) + volume

print("done.  Area={0},  Ribbon={1}".format(totalarea,totalribbon))

