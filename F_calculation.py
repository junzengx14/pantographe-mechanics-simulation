print('To calculate F')
F = numpy.zeros((6,6))
for i in range(6):
	for j in range(6):
		temp = ( S_2[:,i,0] * (S_2[:,j,0]*Matrix_S[:,0,0] + S_2[:,j,1]*Matrix_S[:,0,1]) 
				+S_2[:,i,1] * (S_2[:,j,0]*Matrix_S[:,1,0] + S_2[:,j,1]*Matrix_S[:,1,1]) 
				+S_2[:,i,3] * Matrix_S[:,2,2] * S_2[:,j,3] )
		F[i,j] = sum(temp*IVOL_2)/(l1*l2)