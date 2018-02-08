print('To calculate D')

D_list = numpy.zeros((noip,6,6))
for i in range(2):
	for j in range(3):
		for k in range(2):
			for l in range(3):
				D_list[:,i*3+j,k*3+l] = (U_nabla_1[:,0,j]*Matrix_C_new[:,2*i,2*k]*U_nabla_1[:,0,l] +
										U_nabla_1[:,1,j]*Matrix_C_new[:,2*i+1,2*k]*U_nabla_1[:,0,l] +
										U_nabla_1[:,0,j]*Matrix_C_new[:,2*i,2*k+1]*U_nabla_1[:,1,l] +
										U_nabla_1[:,1,j]*Matrix_C_new[:,2*i+1,2*k+1]*U_nabla_1[:,1,l])
D = numpy.zeros((6,6))
for i in range(6):
	for j in range(6):
		D[i,j] = sum(D_list[:,i,j]*IVOL[:])/(l1*l2)