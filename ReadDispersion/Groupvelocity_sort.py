# calculating acoustic and optical phonon group velocities from dispersion curves 
import numpy as np 
import matplotlib.pyplot as plt
	
def disper_read(disper):
	disper = np.loadtxt(disper)
	print(disper.shape)
	return disper

def Veloc(x,y):
	# x = disper[:,0]
	# y = disper[:,1]
	klist=[]
	lx = len(x)
	for i in range(1,lx):
		k = abs((y[i]-y[i-1])/(x[i]-x[i-1]))
		# print(k)
		klist.append(k)
	# print(len(klist))
	# plt.scatter(y[1:],klist)
	# plt.show()
	return y[1:],klist

def Plot(x,y,c,xmin,xmax,ymin,ymax):
	plt.rc('font', family='Times New Roman', size=16)
	plt.plot(x,y,c)
	plt.xlabel("Frequency (THz)")
	plt.ylabel("Group Velocity (m/s)")
	plt.xlim(xmin,xmax)
	plt.ylim(ymin,ymax)
	return


#---------program main----------#
# atomic number
Natom = 3
xmin,xmax = 0,12 #THz
ymin,ymax = 0,12 
if __name__ == '__main__':

	disper = disper_read('sort_disper.txt')
	# acoustic
	for i in range(1,Natom*3+1):
		if i<=3:
			f,v=Veloc(disper[:,0],disper[:,i])
			Plot(f,v,'b*',xmin,xmax,ymin,ymax )
		elif i>3:
			f,v=Veloc(disper[:,0],disper[:,i])
			Plot(f,v,'r*',xmin,xmax,ymin,ymax )			
	plt.show()





