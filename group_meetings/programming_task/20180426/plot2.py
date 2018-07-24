#plot2: adding in error bars
import matplotlib.pyplot as plt

x = [0.0,0.2,1.0,3.0,5.0]
y = [0.79,0.69,0.49,0.14,0.05]
e = [0.01,0.03,0.04,0.02,0.00]
print(x,y,e)
plt.title("Concentration-dependence inhibition of\nBax-mediated liposomal pore formation")
plt.xlabel('ABT-199 (µM)')
plt.ylabel('CB-Dextran Release (%)')

plt.errorbar(x,y, yerr=e, c='r', marker='o', capsize=3)
plt.show()

