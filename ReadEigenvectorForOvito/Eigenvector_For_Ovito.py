# Read position from gulp outfile
import numpy as np
import pandas as pd
def read_index(OUTfile,k_number,Atomic_number=240):

	with open(OUTfile,'r') as out:
		# print(out.read())
		for index, line in enumerate(out,1):
			if 'Final fractional' in line:
				print(line,index)
				i = index

			if 'Final Cartesian lattice vectors' in line:
				print(line,index)
				j = index

			if 'Phonon Calculation' in line:
				print(line,index)
				p = index

			if 'K point      '+str(k_number) in line:
				print(line,index)
				k_index = index

	return i, j, p, k_index

def write_position(OUTfile,positionfile,i,j):
	with open(OUTfile,'r') as out, open(positionfile,'w') as position:
		for index, line in enumerate(out,1):
			if index>=i+6 and index<=j-3:
				# print(line)
				position.write(line)
	return


# Read gamma point eigen vector

def read_gamma(OUTfile,k_index,fmin,fmax,Atomic_number=240):
	block = Atomic_number*3

	for n_block in range(Atomic_number/2):
		f = np.loadtxt(OUTfile,skiprows=k_index+3+n_block*(block+9),max_rows=1,usecols = (1,2,3,4,5,6)).reshape(1,6)
		v = np.loadtxt(OUTfile,skiprows=k_index+10+n_block*(block+9),max_rows=block,usecols = (2,3,4,5,6,7))
		# print(f.shape,v.shape)
		fv = np.vstack((f/33.36,v))
		# print(fv)
		for i in range(6):
			if fv[0,i]>=fmin and fv[0,i]<=fmax:
				# print(fv[1:,i])
				fv0 = fv[1:,i].reshape(Atomic_number,3)
				np.savetxt('kpoint_1_column'+str(i)+'_fre_'+str(fv[0,i])+'fv.dat',fv0,'%6f %6f %6f')
		
	return

# Read other points eigen vector

def other_point(OUTfile,k_number,k_index,fmin,fmax,Atomic_number=240):
	block = Atomic_number*3
	for n_block in range(Atomic_number):
		f = np.loadtxt(OUTfile,skiprows=k_index+3+n_block*(block+11),max_rows=1,usecols = (1,2,3)).reshape(1,3)
		v = np.loadtxt(OUTfile,skiprows=k_index+13++n_block*(block+11),max_rows=block,usecols = (2,4,6)) # real of complex
		# print(f.shape,v.shape)
		fv = np.vstack((f/33.36,v))
		# print(fv)
		for i in range(3):
			if fv[0,i]>=fmin and fv[0,i]<=fmax:
				fv1 = fv[1:,i].reshape(Atomic_number,3)
				np.savetxt('kpoint_'+str(k_number)+'_column'+str(i)+'_fre_'+str(fv[0,i])+'fv.dat',fv1,'%6f %6f %6f')
	return



def write_ovito(positionfile,eigenvectorfile,ovitofile,Atomic_number):

	position = np.loadtxt(positionfile,dtype=str,usecols=(1,3,4,5))
	eigenvector = np.loadtxt(eigenvectorfile)
	pos_eigen = np.hstack((position,eigenvector))
	# print(pos_eigen)
	with open(ovitofile,'w') as for_eigenvector:
		for_eigenvector.write('         ')
		for_eigenvector.write(str(Atomic_number))
		for_eigenvector.write('\n')
		for_eigenvector.write(' Mo S Se\n')
		for i in range(Atomic_number):
			for j in range(7):
				for_eigenvector.write(str(pos_eigen[i][j])+'      ')
			for_eigenvector.write('\n')

	return



# Main Program

def main():

	print('\n',10*'+','Start',10*'+','\n')
	# freqnency range (THz)
	fmin, fmax = [0.5,0.75] 
	Atomic_number = 240
	k_number = 5 #which k point number
	i, j, p, k_index= read_index('OUTmos2',k_number,Atomic_number)
	# 1. obtain the position from outfile
	write_position('OUTmos2','position_mos2.dat',i,j)
	# 2. obtain the eigen vector form outfile
	if k_number == 1:
		read_gamma('OUTmos2',k_index,fmin,fmax,Atomic_number)
	else:
		other_point('OUTmos2',k_number,k_index,fmin,fmax,Atomic_number)
	return


if __name__ == '__main__':
	main()
	print('\n',10*'+','position file and eigen file ... End!',10*'+','\n')



# 3. write ovito file for visualization

print('\n',10*'+','write ovito file!',10*'+','\n')

write_ovito('position_mos2.dat',
			'kpoint_5_column1_fre_0.5836330935251798fv.dat',
			'kpoint_5_column1_fre_0.5836330935251798_ovito.dat',
			Atomic_number=240)