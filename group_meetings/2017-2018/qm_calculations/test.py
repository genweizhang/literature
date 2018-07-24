import numpy as np
import sys
write = sys.stdout.write
from read_fcidump import *
from matrix_print import *

integrals = ElectronIntegrals()
integrals.read_from_fcidump("FCIDUMP")
NOrb = integrals.NOrb 
NEle = integrals.NEle 
print("NOrb=", NOrb)
print("NEle=", NEle)
ENuc = integrals.nuclear_repulsion_energy
print("ENuc=", ENuc)

#one-electron energy
E1 = 0.0
for i in range(0, int(NEle/2)):
	E1 += 2*integrals.one_e_integrals[i,i]
print("E1=", E1)

#two-electron energy
EJ = 0.0
EK = 0.0
for j in range(0, int(NEle/2)):
	for i in range(0, int(NEle/2)):
		EJ += 2.0*integrals.two_e_integrals[i,i,j,j]
		EK += 1.0*integrals.two_e_integrals[i,j,i,j]
print("EJ=", EJ, "EK=", EK)

#total energy
ETot = ENuc + E1 + EJ - EK
print("ETot=", ETot)

#coulomb and exchange matrices
J_matrix = np.zeros((NOrb, NOrb))
K_matrix = np.zeros((NOrb, NOrb))
F_matrix = np.zeros((NOrb, NOrb))
for p in range(0, NOrb):
	for q in range(0, NOrb):
		for i in range(0,int(NEle/2)):
			J_matrix[p,q] += 2.0*integrals.two_e_integrals[p,q,i,i]
			K_matrix[p,q] += 1.0*integrals.two_e_integrals[p,i,q,i]

#F = h + J - K
F_matrix = np.add(integrals.one_e_integrals, J_matrix)
F_matrix = np.subtract(F_matrix, K_matrix)
matrix_print_2d(F_matrix, 6, "Fock matrix")
		
		








