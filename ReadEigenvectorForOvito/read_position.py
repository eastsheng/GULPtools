# Read position from gulp outfile

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

	return i, j, k_index

def write_position(OUTfile,positionfile,i,j):
	with open(OUTfile,'r') as out, open(positionfile,'w') as position:
		for index, line in enumerate(out,1):
			if index>=i+6 and index<=j-3:
				# print(line)
				position.write(line)
	return


# Main Program
print('\n',10*'+','Start',10*'+','\n')
Atomic_number = 240
k_number = 1 #which k point number
i, j, k_index= read_index('OUTmos2',k_number,Atomic_number)
write_position('OUTmos2','position_mos2.dat',i,j)


print('\n',10*'+','End!',10*'+','\n')
