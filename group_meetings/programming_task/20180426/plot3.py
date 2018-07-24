# plot3: third is reading in the text file into arrays
# all the 'print' functions are for debugging purposes

import numpy as np

data = np.loadtxt(fname='binding-assay-2.txt', delimiter='  ')
print(data)

x,y,e = [],[],[]
print(x,y,e)

for n in range(0,5):
	x.append(data[n][0])
	y.append(data[n][1])
	e.append(data[n][2])

print(x,y,e)


