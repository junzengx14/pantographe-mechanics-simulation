print('To calculate H')
H_list = numpy.zeros((noip,12,12))

for i in range(2):
	for j in range(6):
		for k in range(2):
			for l in range(6):
				H_list[:,i*6+j,k*6+l] = (U_nabla_2[:,0,j]*Matrix_C_new[:,2*i,2*k]*U_nabla_2[:,0,l] +
										U_nabla_2[:,1,j]*Matrix_C_new[:,2*i+1,2*k]*U_nabla_2[:,0,l] +
										U_nabla_2[:,0,j]*Matrix_C_new[:,2*i,2*k+1]*U_nabla_2[:,1,l] +
										U_nabla_2[:,1,j]*Matrix_C_new[:,2*i+1,2*k+1]*U_nabla_2[:,1,l])
H = numpy.zeros((12,12))
for i in range(12):
	for j in range(12):
		H[i,j] = sum(H_list[:,i,j]*IVOL_2[:])/(l1*l2)
