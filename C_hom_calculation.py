Scalar = numpy.zeros((len(Charge),len(Charge)))
Stiffness = numpy.zeros((len(Charge),len(Charge)))
for i,charge in enumerate(Charge): 
    Scalar[i,i] = 2*float(odb.steps['Step-'+charge].historyRegions['Assembly ASSEMBLY'].historyOutputs['ALLSE'].data[0][1]) 

Stiffness = numpy.array([[sum(S[:,0,0]*IVOL[:]), sum(S[:,1,0]*IVOL[:]), 0.0],
						   [sum(S[:,0,1]*IVOL[:]), sum(S[:,1,1]*IVOL[:]), 0.0],
						   [0.0					 , 0.0					, sum(S[:,2,3]*IVOL[:]*sqrt(2))]]) 
Stiffness = Stiffness/(l1*l2*Amp)
Stiffness[numpy.abs(Stiffness)< 10**-8] = 0 
print(' la matrice de raideur homogeneisee C hom',Stiffness_2)
