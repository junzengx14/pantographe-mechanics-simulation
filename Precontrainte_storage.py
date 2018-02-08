# Calculate the initial deplacement by the reference to the pinned point
u_ini = numpy.zeros((non,2,3))
u_ini[:,0,0] = Coordinates[:,0] - referencepoint[0]
u_ini[:,1,1] = Coordinates[:,1] - referencepoint[1]
u_ini[:,0,2] = (Coordinates[:,1] - referencepoint[1])/sqrt(2)
u_ini[:,1,2] = (Coordinates[:,0] - referencepoint[0])/sqrt(2)

# Calculate u_1 by using the substraction 
u_1 = numpy.transpose(U,(0,2,1)) - u_ini # Allouer directement avec les bons axes
elementslist = t.elements

# lanuch the interpolation for u_1 from nodes to integration points
u_1_inter = numpy.zeros((noip,2,3))
for i in xrange(noe):
    element_temp = elementslist[i]
    for l in range(4):
        # dummy average method
        adding=(u_1[element_temp.connectivity[0],:,:] + u_1[element_temp.connectivity[1],:,:] +
            	u_1[element_temp.connectivity[2],:,:] + u_1[element_temp.connectivity[3],:,:] )
        u_1_inter[4*i+l,:,:] = adding/4

# Compute the average deplacement by adding up all areas associated with each integration point
u_1_aver = numpy.zeros((2,3))
for i in range(2):
    for j in range(3):
        u_1_aver[i][j] = sum(u_1_inter[:,i,j]*IVOL[:])
u_1_aver = u_1_aver/area

print('average displacement in ordre 1',u_1_aver)
# Calculate U_nabla_1
# Stop subtracting the average displacement according to the antisymmetry
U_nabla_1 = u_1_inter

# Construction of matrix U_nabla_1
Charge = ['K111','K221','K121','K112','K222','K122']
matrix_nabla = numpy.zeros((len(Charge),noip,3,6)) 

for i in range(len(Charge)):
    matrix_nabla[i,:,0,0:3] = U_nabla_1[:,0,0:3]
    matrix_nabla[i,:,2,0:3] = U_nabla_1[:,1,0:3]
    matrix_nabla[i,:,1,3:6] = U_nabla_1[:,1,0:3]
    matrix_nabla[i,:,2,3:6] = U_nabla_1[:,0,0:3]
    
# Construction of pre-deformation
Epsilon = numpy.zeros((len(Charge),noip,3))
for i in range(len(Charge)):
    Epsilon[i,:,:] = matrix_nabla[i,:,:,i]

# Sigma 11, Sigma 22, Sigma 12  
Sigma = numpy.zeros((len(Charge),noip,4))
for i in range(len(Charge)):
    for j in xrange(noip):
        element_number = j/4
        Sigma[i,j,0:3] = numpy.dot(Matrix_C[element_number],Epsilon[i,j,:])
# Sigma 11, Sigma 22, Sigma33, Sigma 12
Sigma[:,:,3] = Sigma[:,:,2]
for i in range(len(Charge)):
    for j in xrange(noip):
        element_number = j/4
        Sigma[i,j,2] = ((Sigma[i,j,0]+Sigma[i,j,1])*
    		(1-Matrix_S[element_number,0,0]*2/Matrix_S[element_number,2,2]))

#Storage integration points' stress to unf files
print('Storage integration points stress to unf files')

for i in range(4):
    for j in range(6):
        temp = FortranFile('prestress'+str(i+1)+str(j+1)+'.unf','w')
        for k in xrange(noip):
            temp.write_record(numpy.float32(Sigma[j][k][i]))
        temp.close()