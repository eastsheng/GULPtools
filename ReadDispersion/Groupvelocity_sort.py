import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
class GroupVeloc(object):
	"""docstring for GroupVeloc"""
			
	def disper_read(self,disper):
		self.disper = np.loadtxt(disper)
		print(self.disper.shape)
		return

	def veloc(self,Natom=3):
		x = self.disper[:,0]
		for i in range(1,Natom*3+1):
			y = self.disper[:,i]
			plt.plot(x,y)
		
		plt.show()

		return 


if __name__ == '__main__':

	gv = GroupVeloc()
	gv.disper_read('sort_disper.txt')
	gv.veloc()


