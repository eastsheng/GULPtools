# gulp dos--xx.dens
import numpy as np
import matplotlib.pyplot as plt
class DosPlot(object):
	"""docstring for ClassName"""
	def readdos(self,fdos):
		self.dos = np.loadtxt(fdos)
		print(self.dos.shape)
		return
	def plotdos(self,xmin,xmax,ymin,ymax,linewidth=2,THz=True,save=True):
		x = self.dos[:,0]
		y = self.dos[:,1]
		y = y/max(y)
		plt.rc('font',family='Times New Roman',size=16)
		fig,ax = plt.subplots(figsize = (8,6))
		fig.subplots_adjust(bottom=0.2,left=0.2)
		# plt.plot(x,y,'b',linewidth=linewidth)
		if THz==True:
			x = x/33.36
			ax.set_xlabel('Frequency (THz)',fontsize=32,fontweight='bold')

		else:
			x = x 
			ax.set_xlabel('Frequency (cm${}^{-1}$))',fontsize=32,fontweight='bold')
		
		ax.set_ylabel('Density of state',fontsize=32)
		plt.plot(x,y,'b',linewidth=linewidth)
		plt.xlim(xmin,xmax)
		plt.ylim(ymin,ymax)	
		if save == True:
			plt.savefig('dos.png',dpi=300)
		plt.show()
		return

d = DosPlot()
xmin,xmax = [0,500]
ymin,ymax = [0,1.1]
linewidth = 2
THz = False
save=True
if __name__ == '__main__':

	d.readdos("dos.dens")
	d.plotdos(xmin,xmax,ymin,ymax,linewidth,THz,save)