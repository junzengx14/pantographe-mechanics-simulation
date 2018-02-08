for i in range(6):
    openOdb('Job_ordre_2_K'+str(i+1)+'.odb')
Charge = ['K111','K221','K121','K112','K222','K122']

#initialisation
E_2 = numpy.zeros((noip,6,4))
S_2 = numpy.zeros((noip,6,4))
U_2 = numpy.zeros((non,2,6))
IVOL_2 = numpy.zeros(noip)
EVOL_2 = numpy.zeros(noe)
Coordinates_2 = numpy.zeros((non,3))

# Read data from six odb files
# number of integration points, elements, nodes remain constant in deux differents post-calculation
for i,charge in enumerate(Charge):
	odb = session.openOdb('Job_ordre_2_K'+str(i+1)+'.odb')
	Eodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['E' ].values
	Sodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['S' ].values
	Uodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['U' ].values
	for l in xrange(noip):
		E_2[l,i,:] = Eodb[l].data
		S_2[l,i,:] = Sodb[l].data
	for l in xrange(non):
		U_2[l,:,i] = Uodb[l].data
odb = session.openOdb('Job_ordre_2_K1.odb')
IVOLodb = odb.steps['Step-'+'K111'].frames[1].fieldOutputs['IVOL'].values
for i in xrange(noip):
	IVOL_2[i] = IVOLodb[i].data
EVOLodb = odb.steps['Step-'+'K111'].frames[1].fieldOutputs['EVOL'].values
for i in xrange(noe):
	EVOL_2[i] = EVOLodb[i].data
NodeArraySet=t.nodes 
for i in xrange(non):
	Coordinates_2[i] = NodeArraySet[i].coordinates