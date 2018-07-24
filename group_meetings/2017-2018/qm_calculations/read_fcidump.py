import numpy as np
import sys
write = sys.stdout.write

class ElectronIntegrals():

	def __int__(self):
		#doing nothing
		print("Initialize the class")
	
	def read_from_fcidump(self, fcidumpfile):

		fcif = open(fcidumpfile, "r")				
		for line in fcif.readlines():
			cols  = line.split()
			ncols = len(cols)
			if ncols == 5 and cols[0] == '&FCI':
				#This lines reads "&FCI NORB= 10,NELEC= 12,MS2= 0,"
				col2 = cols[2]
				self.NOrb=int(col2[:(col2.find(","))])
				col3 = cols[3]
				self.NEle=int(col3[:(col3.find(","))])
				NOrb = self.NOrb
				self.one_e_integrals = np.zeros((NOrb,NOrb))
				self.two_e_integrals = np.zeros((NOrb,NOrb,NOrb,NOrb))
			elif ncols == 5 and cols[1] == '0' and cols[2] == '0':
				self.nuclear_repulsion_energy = float(cols[0])   
			elif ncols == 5 and cols[3] == '0' and cols[4] == '0':
				p, q = int(cols[1])-1, int(cols[2])-1
				self.one_e_integrals[p,q] = float(cols[0])
				self.one_e_integrals[q,p] = float(cols[0])
			elif ncols == 5:
				p, q = int(cols[1])-1, int(cols[2])-1
				s, t = int(cols[3])-1, int(cols[4])-1
				self.two_e_integrals[p,q,s,t] = float(cols[0]) 
				self.two_e_integrals[q,p,s,t] = float(cols[0]) 
				self.two_e_integrals[p,q,t,s] = float(cols[0]) 
				self.two_e_integrals[q,p,t,s] = float(cols[0]) 
				self.two_e_integrals[s,t,p,q] = float(cols[0]) 
				self.two_e_integrals[s,t,q,p] = float(cols[0]) 
				self.two_e_integrals[t,s,p,q] = float(cols[0]) 
				self.two_e_integrals[t,s,q,p] = float(cols[0]) 

