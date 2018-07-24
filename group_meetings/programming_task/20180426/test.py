#8 lines of code!!

import numpy as np
import matplotlib.pyplot as plt

x,y,e = np.loadtxt(fname='binding-assay-2.txt',unpack=True )

plt.title("Concentration-dependence inhibition of\nBax-mediated liposomal pore formation")
plt.xlabel('ABT-199 (µM)')
plt.ylabel('CB-Dextran Release (%)')

plt.errorbar(x,y, yerr=e, c='r', marker='o', capsize=5)
plt.show()

