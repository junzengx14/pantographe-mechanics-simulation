area = mdb.models[modelname].rootAssembly.getArea(f)
odb = openOdb('Job_ordre_1.odb')
Charge = ['E11','E22','E12']
#intereting numbers
##Attention : the number of integration points and nodes are slightly different
noip = len(odb.steps['Step-E11'].frames[1].fieldOutputs['E'].values)
print('number of total integration points', noip)
non = len(odb.steps['Step-E11'].frames[1].fieldOutputs['U'].values)
print('number of total nodes', non)
noe = len(odb.steps['Step-E11'].frames[1].fieldOutputs['EVOL'].values)
print('number of total elements', noe)
#initialisation
E = numpy.zeros((noip,3,4))
S = numpy.zeros((noip,3,4))
U = numpy.zeros((non,3,2))
IVOL = numpy.zeros(noip)
EVOL = numpy.zeros(noe)
Coordinates = numpy.zeros((non,3)) ##t is the database instance (configurated in each model)
##extract data from the odb file
for i,charge in enumerate(Charge):
    Eodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['E' ].values
    Sodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['S' ].values
    Uodb = odb.steps['Step-'+charge].frames[1].fieldOutputs['U' ].values
    for l in xrange(noip):
    	E[l,i,:] = Eodb[l].data
    	S[l,i,:] = Sodb[l].data
    for l in xrange(non):
       	U[l,i,:] = Uodb[l].data
IVOLodb = odb.steps['Step-'+'E11'].frames[1].fieldOutputs['IVOL'].values
for i in xrange(noip):
	IVOL[i] = IVOLodb[i].data
EVOLodb = odb.steps['Step-'+'E11'].frames[1].fieldOutputs['EVOL'].values
for i in xrange(noe):
	EVOL[i] = EVOLodb[i].data
NodeArraySet=t.nodes 
for i in xrange(non):
	Coordinates[i] = NodeArraySet[i].coordinates