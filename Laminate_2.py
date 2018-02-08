# -*- coding: mbcs -*-
from part import *
from material import *
from section import *
from assembly import *
from step import *
from interaction import *
from load import *
from mesh import *
from optimization import *
from job import *
from sketch import *
from visualization import *
from connectorBehavior import *
Young_1 =  1
Poisson_1 = 0.4
#downside material
Young_2 = 10.0
Poisson_2 = -0.9

#Geometric settings
l2 = 20
l1_1 = 0.5
l1_2 = 1.5
l1 = l1_1 + l1_2
Amp = 1.0
BCSym = 1

#mesh settings
horizontal_mesh_number_left = 15
horizontal_mesh_number_right = 60
vertical_mesh_number = 5
m = mdb.Model(name='Laminate_2', modelType=STANDARD_EXPLICIT)
m.ConstrainedSketch(name='__profile__', sheetSize=200.0)
m.sketches['__profile__'].rectangle(point1=(l1, 0.0), point2=(0.0, l2))
m.Part(dimensionality=TWO_D_PLANAR, name='Tranches', type=DEFORMABLE_BODY)
m.parts['Tranches'].BaseShell(sketch=m.sketches['__profile__'])
del m.sketches['__profile__']
#divide into two parts
mdb.models['Laminate_2'].parts['Tranches'].PartitionEdgeByParam(edges=
    mdb.models['Laminate_2'].parts['Tranches'].edges.findAt((l1/4, l2, 0.0), ), parameter=l1_1/(l1_1+l1_2))
mdb.models['Laminate_2'].parts['Tranches'].PartitionEdgeByParam(edges=
    mdb.models['Laminate_2'].parts['Tranches'].edges.findAt((l1/4, 0.0, 0.0), ), parameter=l1_1/(l1_1+l1_2))
m.parts['Tranches'].PartitionFaceByShortestPath(faces=m.parts['Tranches'].faces.findAt(((l1/2, l2/2, 0.0), )), 
	point1=mdb.models['Laminate_2'].parts['Tranches'].vertices[1], point2=
    mdb.models['Laminate_2'].parts['Tranches'].vertices[4] )
#material definitions
m.Material(name='Material-Left')
m.materials['Material-Left'].Elastic(table=((Young_1, Poisson_1), ))
m.Material(name='Material-Right')
m.materials['Material-Right'].Elastic(table=((Young_2, Poisson_2), ))
#naming haut bas gauche droite
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((0, l2/2, 0.0), )), 
	name='gauche')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1, l2/2, 0.0), )), 
	name='droite')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1_1/2, 0.0, 0.0), ), ((l1_1+l1_2/2, 0.0, 0.0), ), ), 
	name='bas')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1_1/2, l2, 0.0), ), ((l1_1+l1_2/2, l2, 0.0), ), ), 
	name='haut')
#name two surfaces : Surface-Down, Surface-Up, Global
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1_1/2, l2/2, 0.0), )), name='Surface-Left')
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1_1+l1_2/2, l2, 0.0), )), name='Surface-Right')
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1_1/2, l2/2, 0.0), ), ((l1_1+l1_2/2, l2, 0.0), ), ), 
	name='Cellule')
#assign material
m.HomogeneousSolidSection(material='Material-Left', name='Section-Left', thickness=1.0)
m.HomogeneousSolidSection(material='Material-Right', name='Section-Right', thickness=1.0)
m.parts['Tranches'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
	region=m.parts['Tranches'].sets['Surface-Left'], 
	sectionName='Section-Left', thicknessAssignment=FROM_SECTION)
m.parts['Tranches'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, 
	region=m.parts['Tranches'].sets['Surface-Right'], 
    sectionName='Section-Right', thicknessAssignment=FROM_SECTION)

m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(
	((l1_1/2, 0.0 , 0.0), ), ((l1_1/2, l2, 0.0), ), 
 ), number=horizontal_mesh_number_left)
m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(
	((l1_1+l1_2/2, 0.0, 0.0), ), ((l1_1+l1_2/2, l2, 0.0),),  
 ), number=horizontal_mesh_number_right)
m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(
	((0.0,l2/2,0.0), ), ((l1_1, l2/2, 0.0), ),
 ((l1, l2/2, 0.0), ), ), number=vertical_mesh_number)
mdb.models['Laminate_2'].parts['Tranches'].setElementType(elemTypes=(ElemType(elemCode=CPE4, elemLibrary=STANDARD, 
	secondOrderAccuracy=OFF, hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(elemCode=CPE3, 
	elemLibrary=STANDARD)), regions=(
    mdb.models['Laminate_2'].parts['Tranches'].faces.findAt(((l1_1/2, l2/2, 0.0), ), ((l1_1+l1_2/2, l2/2, 0.0), ), ), ))
m.parts['Tranches'].generateMesh()

m.rootAssembly.DatumCsysByDefault(CARTESIAN)
m.rootAssembly.Instance(dependent=ON, name='Tranches-1', 
    part=m.parts['Tranches'])

p = m.parts['Tranches'] 
cc = mdb.models['Laminate_2']
t= cc.rootAssembly.instances['Tranches-1']

f = mdb.models['Laminate_2'].parts['Tranches'].faces

referencepoint = (0.0 , 0.0 , 0.0)

#Creation of Material Sets in a dictionary
Cleft = isotrope2d(Young_1,Poisson_1)
print('matrix of C in the upper surface',Cleft)
Cright = isotrope2d(Young_2,Poisson_2)
print('matrix of C in the lower surface',Cright)
C_left = isotrope2d_nsym(Young_1,Poisson_1)
C_right = isotrope2d_nsym(Young_2,Poisson_2)
S_left = isotrope2d_inverse(Young_1,Poisson_1)
S_right = isotrope2d_inverse(Young_2,Poisson_2)
MaterialSets_C={'Surface-Left':Cleft,'Surface-Right':Cright}
NewMaterialSets_C={'Surface-Left':C_left,'Surface-Right':C_right}
MaterialSets_S={'Surface-Left':S_left,'Surface-Right':S_right}
mdb.models[modelname].rootAssembly.Set(name='Set-1', vertices=
    t.vertices.findAt(((0.0, 0.0, 0.0), )))