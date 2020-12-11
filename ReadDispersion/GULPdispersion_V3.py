# DEAL AND PLOT THE DISPERSION FROM 'GULP' PACKAGE
import numpy as np 
import matplotlib.pyplot as plt
import re
class GulpDisp(object):
	"""Gulp Dispersion"""
	def Readata(self,disp_data,number_atom=96):
		self.disp_data = disp_data
		self.number_branch=number_atom*3
		return 

	def ReadKpoint(self,disp_data,number_atom=96):
		self.disp_data = disp_data
		self.K = 0
		self.number_atom=number_atom
		with open(disp_data,'r')as disp:
			for line in disp:
				if 'Final K point' in line:
					# print(line)
					K =re.findall('K point =   (.*?)  ',line)[0]
					self.K = float(K)
					print('\nk Point path =','[ 0 ,',str(self.K),']\n')
				else:
					pass
		return

	def PlotSinglepath(self,xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True):
		self.data = np.loadtxt(self.disp_data)
		print(self.data.shape)
		# print(self.data)
		# print(len(self.data))
		len_data = len(self.data)
		line_number = int(len_data/self.number_atom/3)
		
		# WaveVector = self.K*(np.unique(self.data[:,0]-1)/(len_data/line_number))
		WaveVector = np.linspace(0,1,line_number)
		Frequency = self.data[:,1].reshape((line_number,self.number_atom*3))
		Frequency = Frequency/33.36 # CM-1 >> THz
		
		print(Frequency.shape)
		print(WaveVector.shape)
		
		# Plot
		plt.rc('font',family='Times New Roman',size=16)
		fig,ax = plt.subplots(figsize = (6,8))
		fig.subplots_adjust(bottom=0.1,left=0.2)
		plt.plot(WaveVector,Frequency,'b',linewidth=linewidth)
		ax.set_xlabel('Wave Vector',fontsize=32,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=32)
		plt.xticks(size=8)
		plt.yticks(size=22)
		plt.xlim(xmin,xmax)
		plt.ylim(ymin,ymax)
		if save == True:
			plt.savefig('fig.png',dpi=dpi)
		plt.show()

		return 


	def PlotMultipath(self,xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True):
		self.data = np.loadtxt(self.disp_data)
		print(self.data.shape)
		# print(self.data)
		# print(len(self.data))
		len_data = len(self.data)
		line_number = int(len_data/self.number_branch)
		self.WaveVector = np.linspace(0,1,line_number).reshape((line_number,1))
		Frequency = self.data[:,1].reshape((line_number,self.number_branch))
		self.Frequency = Frequency/33.36 # CM-1 >> THz	
		# print(Frequency.shape)
		# Plot
		# plt.rc('font',family='Times New Roman')
		fig,ax = plt.subplots(figsize = (6,8))
		fig.subplots_adjust(bottom=0.1,left=0.2)
		plt.plot(self.WaveVector,self.Frequency,'b',linewidth=linewidth)
		ax.set_xlabel('Wave Vector',fontsize=26,fontweight='bold')
		ax.set_ylabel('Frequency (THz)',fontsize=26,fontweight='bold')
		plt.xticks(size=24)
		plt.yticks(size=24)
		plt.xlim(xmin,xmax)
		plt.ylim(ymin,ymax)
		if save == True:
			plt.savefig('fig.png',dpi=dpi)
		plt.show()
		return 

	def save_disper(self,):
		x = self.WaveVector
		y = self.Frequency
		disper = np.hstack((x,y))
		np.savetxt('sort_disper.txt',disper,fmt='%f %f')
		return

# *************Main Program************* #
# The number of atoms in the primitive cell
if __name__ == '__main__':
	# if n==True path is single, else multipath
	n=True
	save_disperion=True
	
	number_atom = 3
	# plot x y range and line width
	xmin,xmax = [0,1]
	ymin,ymax = [0,16]
	linewidth = 2

	gulp = GulpDisp()

	if n==True:

		gulp.ReadKpoint('gulp.disp',number_atom)
		gulp.PlotSinglepath(xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True)
		if save_disperion == True:
			gulp.save_disper()
	else:
		gulp.Readata('25_4x8_defect.disp',number_atom)
		gulp.PlotMultipath(xmin,xmax,ymin,ymax,linewidth,dpi=300,save=True)


	

		
	
