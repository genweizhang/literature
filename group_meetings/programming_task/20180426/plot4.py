#plot4: final plot; combined reading of txt file, along with plotting data and error bars
import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(fname='binding-assay-2.txt', delimiter='  ')

x,y,e = [],[],[]

for n in range(0,5):
        x.append(data[n][0])
        y.append(data[n][1])
        e.append(data[n][2])

plt.title("Concentration-dependence inhibition of\nBax-mediated liposomal pore formation")
plt.xlabel('ABT-199 (µM)')
plt.ylabel('CB-Dextran Release (%)')

plt.errorbar(x,y, yerr=e, c='r', marker='o', capsize=5)
plt.show()

