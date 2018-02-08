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
l1 = 0.025
l2_1 = 0.5
l2_2 = 1.5
l2 = l2_1 + l2_2
Amp = 1.0
BCSym = 1

#mesh settings
vertical_mesh_number_up = 20
vertical_mesh_number_down = 60 
horizontal_mesh_number = 1
m = mdb.Model(name='Laminate', modelType=STANDARD_EXPLICIT)
m.ConstrainedSketch(name='__profile__', sheetSize=200.0)
m.sketches['__profile__'].rectangle(point1=(l1, 0.0), point2=(0.0, l2_1+l2_2))
m.Part(dimensionality=TWO_D_PLANAR, name='Tranches', type=DEFORMABLE_BODY)
m.parts['Tranches'].BaseShell(sketch=m.sketches['__profile__'])
del m.sketches['__profile__']
#divide into two parts
mdb.models['Laminate'].parts['Tranches'].PartitionEdgeByParam(edges=
    mdb.models['Laminate'].parts['Tranches'].edges.findAt((0, l2_2, 0.0), ), parameter=l2_1/(l2_1+l2_2))
mdb.models['Laminate'].parts['Tranches'].PartitionEdgeByParam(edges=
    mdb.models['Laminate'].parts['Tranches'].edges.findAt((l1, l2_2, 0.0), ), parameter=l2_1/(l2_1+l2_2))
m.parts['Tranches'].PartitionFaceByShortestPath(faces=m.parts['Tranches'].faces.findAt(((l1/2, l2_2, 0.0), )), 
	point1=mdb.models['Laminate'].parts['Tranches'].vertices[2], point2=
    mdb.models['Laminate'].parts['Tranches'].vertices[5] )
#material definitions
m.Material(name='Material-Up')
m.materials['Material-Up'].Elastic(table=((Young_1, Poisson_1), ))
m.Material(name='Material-Down')
m.materials['Material-Down'].Elastic(table=((Young_2, Poisson_2), ))
#naming haut bas gauche droite
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1/2, l2_1+l2_2, 0.0), )), 
	name='haut')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1/2, 0.0, 0.0), )), 
	name='bas')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((0.0, l2_2/2, 0.0), ), ((0.0, l2_2+l2_1/2, 0.0), ), ), 
	name='gauche')
m.parts['Tranches'].Set(edges=m.parts['Tranches'].edges.findAt(((l1, l2_2/2, 0.0), ), ((l1, l2_2+l2_1/2, 0.0), ), ), 
	name='droite')
#name two surfaces : Surface-Down, Surface-Up, Global
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1/2, l2_2/2, 0.0), )), name='Surface-Down')
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1/2, l2_2+l2_1/2, 0.0), )), name='Surface-Up')
m.parts['Tranches'].Set(faces=m.parts['Tranches'].faces.findAt(((l1/2, l2_2/2, 0.0), ), ((l1/2, l2_2+l2_1/2, 0.0), ), ), 
	name='Cellule')
#assign material
m.HomogeneousSolidSection(material='Material-Down', name='Section-Down', thickness=1.0)
m.HomogeneousSolidSection(material='Material-Up', name='Section-Up', thickness=1.0)
m.parts['Tranches'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=m.parts['Tranches'].sets['Surface-Up'], 
	sectionName='Section-Up', thicknessAssignment=FROM_SECTION)
m.parts['Tranches'].SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=m.parts['Tranches'].sets['Surface-Down'], 
    sectionName='Section-Down', thicknessAssignment=FROM_SECTION)

m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(((0, l2_2+l2_1/2, 0.0), ), ((l1, l2_2+l2_1/2, 0.0), ), 
 ), number=vertical_mesh_number_up)
m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(((0, l2_2/2, 0.0), ), ((l1, l2_2/2, 0.0),),  
 ), number=vertical_mesh_number_down)
m.parts['Tranches'].seedEdgeByNumber(constraint=FINER, edges=m.parts['Tranches'].edges.findAt(((l1/2,0,0), ), ((l1/2, l2_2, 0.0), ),
 ((l1/2, l2_1+l2_2, 0.0), ), ), number=horizontal_mesh_number)
mdb.models['Laminate'].parts['Tranches'].setElementType(elemTypes=(ElemType(elemCode=CPE4, elemLibrary=STANDARD, secondOrderAccuracy=OFF, 
    hourglassControl=DEFAULT, distortionControl=DEFAULT), ElemType(elemCode=CPE3, elemLibrary=STANDARD)), regions=(
    mdb.models['Laminate'].parts['Tranches'].faces.findAt(((l1/2, l2_2/2, 0.0), ), ((l1/2, l2_2+l2_1, 0.0), ), ), ))
m.parts['Tranches'].generateMesh()

m.rootAssembly.DatumCsysByDefault(CARTESIAN)
m.rootAssembly.Instance(dependent=ON, name='Tranches-1', 
    part=m.parts['Tranches'])

p = m.parts['Tranches'] 
cc = mdb.models['Laminate']
t= cc.rootAssembly.instances['Tranches-1']

f = mdb.models['Laminate'].parts['Tranches'].faces

referencepoint = (0.0 , 0.0 , 0.0)

#Creation of Material Sets in a dictionary
Cup = isotrope2d(Young_1,Poisson_1)
print('matrix of C in the upper surface',Cup)
Cdo = isotrope2d(Young_2,Poisson_2)
print('matrix of C in the lower surface',Cdo)
C_up = isotrope2d_nsym(Young_1,Poisson_1)
C_down = isotrope2d_nsym(Young_2,Poisson_2)
S_up = isotrope2d_inverse(Young_1,Poisson_1)
S_down = isotrope2d_inverse(Young_2,Poisson_2)
MaterialSets_C={'Surface-Up':Cup,'Surface-Down':Cdo}
NewMaterialSets_C={'Surface-Up':C_up,'Surface-Down':C_down}
MaterialSets_S={'Surface-Up':S_up,'Surface-Down':S_down}
mdb.models[modelname].rootAssembly.Set(name='Set-1', vertices=
    t.vertices.findAt(((0.0, 0.0, 0.0), )))