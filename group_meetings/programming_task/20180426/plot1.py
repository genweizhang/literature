#plot1: first directly plotting the information given, excluding error bars

import matplotlib.pyplot as plt
x = [0.0,0.2,1.0,3.0,5.0]
y = [0.79,0.69,0.49,0.14,0.05]
print(x,y)
plt.title("Concentration-dependence inhibition of\nBax-mediated liposomal pore formation")
plt.xlabel('ABT-199 (µM)')
plt.ylabel('CB-Dextran Release (%)')

plt.plot(x,y, c='r', marker='o')
plt.show()

