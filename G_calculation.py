print('To calculate G')
print('To calculate U_nabla_2')
#interpolation of U to U_inter at intergration points
elementslist = t.elements
U_inter = numpy.zeros((noip,2,6))
for i in xrange(noe):
    element_temp = elementslist[i]
    for l in range(4):
        if l == 0:
            a1 = -sqrt(3)/3
            a2 = -sqrt(3)/3
        elif l == 1:
            a1 =  sqrt(3)/3
            a2 = -sqrt(3)/3
        elif l == 2:
            a1 = -sqrt(3)/3
            a2 =  sqrt(3)/3
        elif l == 3:
            a1 =  sqrt(3)/3
            a2 =  sqrt(3)/3
        U_inter[4*i+l,:,:] =  ( 
            U_2[element_temp.connectivity[0],:,:]*(1.0/4)*(1.0-a1)*(1.0-a2) + 
            U_2[element_temp.connectivity[1],:,:]*(1.0/4)*(1.0+a1)*(1.0-a2) + 
            U_2[element_temp.connectivity[2],:,:]*(1.0/4)*(1.0+a1)*(1.0+a2) + 
            U_2[element_temp.connectivity[3],:,:]*(1.0/4)*(1.0-a1)*(1.0+a2))
        
U_inter_aver = numpy.zeros((2,6))
for i in range(2):
	for j in range(6):
		U_inter_aver[i,j] = sum(U_inter[:,i,j]*IVOL_2[:])/area
# antisymmetry
U_inter_aver[1,0] = 0.0
U_inter_aver[1,1] = 0.0
U_inter_aver[0,2] = 0.0
U_inter_aver[0,3] = 0.0
U_inter_aver[0,4] = 0.0
U_inter_aver[1,5] = 0.0

print(U_inter_aver)

U_nabla_2 = numpy.zeros((noip,2,6))
for i in range(2):
	for j in range(6):
		U_nabla_2[:,i,j] = U_inter[:,i,j] - U_inter_aver[i,j]

# read stress from the results in the calculation ordre 1
B = numpy.zeros((noip,2,6))
temp = numpy.transpose(S,(0,2,1))
B[:,0,0:3] = temp[:,0,0:3]
B[:,0,3:6] = temp[:,3,0:3]
B[:,1,0:3] = temp[:,3,0:3]
B[:,1,3:6] = temp[:,1,0:3]

#calculate G
G = numpy.zeros((6,6))
for i in range(6):
	for j in range(6):
		temp = numpy.zeros(noip)
		for l in range(2):
			temp = temp + B[:,l,i]*U_nabla_2[:,l,j]
		G[i,j] = sum(temp*IVOL_2)/(l1*l2)

 