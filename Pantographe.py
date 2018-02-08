# -*- coding: mbcs -*-
from __future__ import division
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
from odbAccess import *
import numpy 
import mesh
import math

############  parametres geometriques
## attention a la coherence des parametres entre eux
m= mdb.Model(name='Pantographe', modelType=STANDARD_EXPLICIT)
bb =1.0 

k=1.0 # longeur connexion
pp=2*bb/10 # epaisseur connexion
c=2.0 # diagonale carre  

# r = 0.0003 #0.0005 # 0.0003# rayon du cercle inscrit virtuel dont dependent tous les RdC
# dimensions cellule
l1 = 2*bb+k+(c/2)
l2 = 2*bb # l2 doit etre de meme taille que le 1er terme de l1

# beta = atan (pp/(k/2)) en radian   =   180* ( atan (pp/(k/2))  ) / pi  en degres  
# angles pr RDC en radian
alpha1= atan( ((2*bb)-(c/2))/ 2*bb )  
alpha2= (pi + alpha1 - atan (pp/(k/2)) - pi*0.5 ) /2
alpha3= (0.5*pi-atan (pp/(k/2))-alpha1)/2
alpha4= pi*45.0/180
alpha5= (pi*90/180) - alpha1 

r1=((   sqrt((r*tan(alpha1))**2 + r**2) + r*tan(alpha1)  ) / cos(alpha1)  ) - r
r2=((   sqrt((r*tan(alpha2))**2 + r**2) + r*tan(alpha2)  ) / cos(alpha2)  ) - r
r3=((   sqrt((r*tan(alpha3))**2 + r**2) + r*tan(alpha3)  ) / cos(alpha3)  ) - r
r4=((   sqrt((r*tan(alpha4))**2 + r**2) + r*tan(alpha4)  ) / cos(alpha4)  ) - r
r5=((   sqrt((r*tan(alpha5))**2 + r**2) + r*tan(alpha5)  ) / cos(alpha5)  ) - r

############  parametres materiaux
Ev = 0.001
Young = 1   
Poisson = 0.3

############ parametres maillage
n=5.0
minSizeMesh = 2*pi*r/(3*n) # r ? r/n ? 
maxSizeMesh = l1/50
maxSizeMesh2 = l1/100  # pour les connexions
forme = QUAD  # forme des elements ( TRI pour triangulaire )
elemcodtyp1 = CPE4  # elements quadratiques DefPlanes  ( CPE8R pr quadra , CPE4R pr lineaire)
elemcodtyp2 = CPE3 # elements quadratiques DefPlanes  ( CPE6M  pr quadra  , CPE3 pr lineraire)

############  parametres post processing
Amp = 1.0
BCSym = 1

############ PART rectangle ##############################
m.ConstrainedSketch(name='__profile__', sheetSize=200.0)
pr = mdb.models['Pantographe'].sketches['__profile__']
pr.rectangle(point1=(0.0, l2),point2=(l1, 0.0))
m.Part(dimensionality=TWO_D_PLANAR, name='Part-1', type= DEFORMABLE_BODY)
m.parts['Part-1'].BaseShell(sketch= pr)

#### paramterisation des arretes du rectangle   
p = mdb.models['Pantographe'].parts['Part-1']
e = p.edges

# repere grid point bas gauche
edges = e.findAt(((l1/2,l2, 0.0),))
p.Set(edges=edges, name='haut')
 
edges = e.findAt(((l1,l2/2, 0.0),))
p.Set(edges=edges, name='droite')
   
edges = e.findAt(((l1/2,0.0, 0.0),))
p.Set(edges=edges, name='bas')
   
edges = e.findAt(((0.0,l2/2, 0.0),))
p.Set(edges=edges, name='gauche')

### partition de la geometrie interne       
m.ConstrainedSketch(gridSpacing=5.19, name='__profile__',
sheetSize=207.84, transform= p.MakeSketchTransform(
    sketchPlane=p.faces[0], 
    sketchPlaneSide=SIDE1, sketchOrientation=RIGHT, origin=(0.0, 0.0, 0.0)))
p.projectReferencesOntoSketch(filter=COPLANAR_EDGES, sketch=m.sketches['__profile__'])
mdb.models['Pantographe'].sketches['__profile__'].sketchOptions.setValues(
    gridOrigin=(-l1/2, -l2/2))
pr = mdb.models['Pantographe'].sketches['__profile__']
s = pr.geometry

## repere partition toujours point bas gauche contrairement a letoile
pr.Line(point1=(0.0,c/2),point2=(c/2,0.0))   #a (A-F)
pr.Line(point1=(0.0,-c/2),point2=(c/2,0.0))  #b (A3-F)
pr.Line(point1=(0.0,c/2),point2=(-c/2,0.0))  #c (A-F2)

#* curve a-b  c3
pr.FilletByRadius(curve1= s.findAt((  (c/2)/2, (c/2)/2    )),
curve2=s.findAt((  (c/2)/2, -(c/2)/2   )), 
nearPoint1=((c/2)/2, (c/2)/2), nearPoint2=((c/2)/2, -(c/2)/2), radius=r4)
                  
#* curve c-a  c10
pr.FilletByRadius(curve1= s.findAt((  (c/2)/2, (c/2)/2   )),
curve2=s.findAt((  -(c/2)/2, (c/2)/2   )), 
nearPoint1=((c/2)/2, (c/2)/2), nearPoint2=(-(c/2)/2, (c/2)/2), radius=r4)                  
                                    
pr.Line(point1=((2*bb)+k+(c/2),2*bb-(c/2) ) , point2=(   (2*bb)+k,2*bb  ))  #d (D-C)
pr.Line(point1=((2*bb)+k+(c/2),2*bb-(c/2) ) , point2=(   (2*bb)+k+c,2*bb ))  #e (D-C2)
pr.Line(point1=((2*bb)+k,2*bb) , point2=((2*bb)+k+(c/2),(2*bb)+(c/2) ) ) #f (C-D3) 
                  
#* curve d-e  c9                
pr.FilletByRadius(curve1= s.findAt((  ((2*bb)+k+(c/2)+(2*bb)+k)/2, (2*bb-(c/2)+2*bb)/2   )),
curve2=s.findAt((  ((2*bb)+k+(c/2)+(2*bb)+k+c)/2, (2*bb-(c/2)+2*bb)/2  )), 
nearPoint1=(( (2*bb)+k+(c/2)+(2*bb)+k)/2, (2*bb-(c/2)+2*bb)/2), 
nearPoint2=(((2*bb)+k+(c/2)+(2*bb)+k+c)/2, (2*bb-(c/2)+2*bb)/2   ), radius=r4)                   
                                    
#* curve d-f  c4
pr.FilletByRadius(curve1= s.findAt((  ( (2*bb)+k+(c/2)+(2*bb)+k)/2, (2*bb-(c/2)+2*bb)/2   )),
curve2=s.findAt(( ((2*bb)+k+ (2*bb)+k+(c/2))/2, (2*bb+(2*bb)+(c/2))/2  )), 
nearPoint1=(( (2*bb)+k+(c/2)+(2*bb)+k)/2, (2*bb-(c/2)+2*bb)/2), 
nearPoint2=(((2*bb)+k+ (2*bb)+k+(c/2))/2, (2*bb+(2*bb)+(c/2))/2 ), radius=r4)                   
                                   
pr.Line(point1=(k+(c/2),0.0),point2=((2*bb)+k+(c/2),2*bb-(c/2)))  #m (E-D)                  
pr.Line(point1=(2*bb+k+(c/2),(2*bb)-(c/2)),point2=((c/2)+k+(4*bb),0.0))  #o (D-E2)                  
pr.Line(point1=(0.0,c/2),point2=(2*bb,2*bb))  #p (A-B)   
pr.Line(point1=(0.0,c/2),point2=(-(2*bb),2*bb))  #q (A-B2)
pr.Line(point1=(k+(c/2),0.0),point2=((2*bb)+k+(c/2),-(2*bb)+(c/2)))  #n (E-D2)
pr.Line(point1=(2*bb,2*bb),point2=(0.0,(4*bb)-(c/2)))  #r (B-A2)
                                    
# curve m-o  c11                
pr.FilletByRadius(curve1= s.findAt((  (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+2*bb-(c/2))/2   )),
curve2=s.findAt((  (2*bb+k+(c/2)+(c/2)+k+(4*bb))/2, ((2*bb)-(c/2)+0.0)/2  )), 
nearPoint1=((k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+2*bb-(c/2))/2), 
nearPoint2=((2*bb+k+(c/2)+(c/2)+k+(4*bb))/2, ((2*bb)-(c/2)+0.0)/2  ), radius=r5)                   
                  
# curve q-p  c12                                  
pr.FilletByRadius(curve1= s.findAt((  (0.0+2*bb)/2, ((c/2)+2*bb)/2   )),
curve2=s.findAt((  (0.0-(2*bb))/2, (c/2+2*bb)/2  )), 
nearPoint1=((0.0+2*bb)/2, ((c/2)+2*bb)/2), 
nearPoint2=((0.0-(2*bb))/2, (c/2+2*bb)/2  ), radius=r5)                  
                                   
# curve m-n c2
pr.FilletByRadius(curve1= s.findAt((  (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+-(2*bb)+(c/2))/2   )),
curve2=s.findAt((    (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+2*bb-(c/2))/2    )), 
nearPoint1=(    (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+-(2*bb)+(c/2))/2    )  , 
nearPoint2=(   (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+2*bb-(c/2))/2    ) , radius=r1)                                         

# curve p-r  c1                
pr.FilletByRadius(curve1= s.findAt((  (0.0+2*bb)/2, (c/2+2*bb)/2   )),
curve2=s.findAt((    (2*bb+0.0)/2, (2*bb+(4*bb)-(c/2))/2    )), 
nearPoint1=(    (0.0+2*bb)/2, (c/2+2*bb)/2     )  , 
nearPoint2=(  (2*bb+0.0)/2, (2*bb+(4*bb)-(c/2))/2    ) , radius=r1)   
                                    
pr.Line(point1=(c/2,0.0),point2=(2*bb,2*bb))  #g (F-B)
pr.Line(point1=(c/2,0.0),point2=((c/2)+(k/2),pp))  #i (F-G)
pr.Line(point1=(k+(c/2),0.0),point2=((2*bb)+k,2*bb))  #h (E-C)
pr.Line(point1=((2*bb)+(k/2),(2*bb)-pp),point2=((2*bb)+k,2*bb))  #l (H-C)
pr.Line(point1=((c/2)+(k/2),pp),point2=(k+(c/2),0.0))  #j (G-E)
pr.Line(point1=(2*bb,2*bb),point2=((2*bb)+(k/2),(2*bb)-pp))  #k (B-H)                  
                                    
#curve g-i  c7
pr.FilletByRadius(curve1= s.findAt((  (c/2+2*bb)/2, (0.0+2*bb)/2   )),
curve2=s.findAt((  (c/2+(c/2)+(k/2))/2, (0.0+pp)/2  )), 
nearPoint1=(  (c/2+2*bb)/2, (0.0+2*bb)/2 ) , nearPoint2=(    (c/2+(c/2)+(k/2))/2, (0.0+pp)/2  )  , radius=r3) 
                  
###curve h-l  c6
pr.FilletByRadius(curve1= s.findAt((  (k+(c/2)+(2*bb)+k)/2, (0.0+2*bb)/2   )),
curve2=s.findAt((    ((2*bb)+(k/2)+(2*bb)+k)/2, ((2*bb)-pp+2*bb)/2    )), 
nearPoint1=(    (k+(c/2)+(2*bb)+k)/2, (0.0+2*bb)/2     )  , nearPoint2=(   ((2*bb)+(k/2)+(2*bb)+k)/2, ((2*bb)-pp+2*bb)/2    ) , radius=r3)                    
                  
###curve g-k c5            
pr.FilletByRadius(curve1= s.findAt((  (c/2+2*bb)/2, (0.0+2*bb)/2   )),
curve2=s.findAt((    (2*bb+(2*bb)+(k/2))/2, (2*bb+(2*bb)-pp)/2    )), 
nearPoint1=(    (c/2+2*bb)/2, (0.0+2*bb)/2    )  , nearPoint2=(    (2*bb+(2*bb)+(k/2))/2, (2*bb+(2*bb)-pp)/2     ) , radius=r2)                 

###curve j-h c8
pr.FilletByRadius(curve1= s.findAt((  ((c/2)+(k/2)+k+(c/2))/2, (pp+0.0)/2   )),
curve2=s.findAt((    (k+(c/2)+(2*bb)+k)/2, (0.0+2*bb)/2    )), 
nearPoint1=(    ((c/2)+(k/2)+k+(c/2))/2, (pp+0.0)/2      )  , nearPoint2=(   (k+(c/2)+(2*bb)+k)/2, (0.0+2*bb)/2    ) , radius=r2)
                  
### partitions des diamants                                   
pr.Line(point1=(c/2-r,0.0),point2=(c/2+r,0.0))                   
pr.Line(point1=(c/2+k-r,0.0),point2=(c/2+k+r,0.0))
pr.Line(point1=(2*bb-r,2*bb),point2=(2*bb+r,2*bb))
pr.Line(point1=(2*bb+k-r,2*bb),point2=(2*bb+k+r,2*bb))
                  
                  
                  
p = mdb.models['Pantographe'].parts['Part-1']
p.PartitionFaceBySketch(faces=p.faces.findAt(((0.0, 0.0, 0.0), )),sketch=pr)
###### supprimer la partie vide ######
f = p.faces
index_pantographe = mdb.models['Pantographe'].parts['Part-1'].faces.findAt((l1/4,l2/2,0.0),).index
mdb.models['Pantographe'].parts['Part-1'].RemoveFaces(deleteCells=False, 
    faceList=f[0:index_pantographe]+f[index_pantographe+1:6])

##################  proprietes ###########
m = mdb.models['Pantographe']
p = m.parts['Part-1']
m.Material(name='Material-plein')
m.materials['Material-plein'].Elastic(table=((Young, Poisson),))
m.HomogeneousSolidSection(material='Material-plein', 
name='plein', thickness=None)

## repere point bas gauche                                           
p.Set(faces=m.parts['Part-1'].faces.findAt(((c/2, bb/4, 0.0), )), name='Cellule')
p.SectionAssignment(offset=0.0, offsetField='', offsetType=MIDDLE_SURFACE, region=p.sets['Cellule'], sectionName='plein',thicknessAssignment=FROM_SECTION)

################ Assembly #############
m.rootAssembly.DatumCsysByDefault(CARTESIAN)
m.rootAssembly.Instance(dependent=ON, name='Part-1-1', part=m.parts['Part-1'])                                                                        
                          
###################### mesh ##################
# repere Grid ( bas gauche ) 
                         
#g
pickedEdges = e.findAt(((      (c/2+2*bb)/2, (0.0+2*bb)/2, 0.0      ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)                            
# i
pickedEdges1 = e.findAt(((      (c/2+(c/2)+(k/2))/2, (0.0+pp)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER) 
# j
pickedEdges2 = e.findAt(((      ((c/2)+(k/2)+k+(c/2))/2, (pp+0.0)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER)
# k
pickedEdges2 = e.findAt(((      (2*bb+(2*bb)+(k/2))/2, (2*bb+(2*bb)-pp)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=SINGLE, end1Edges=pickedEdges1, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER)
# l
pickedEdges1 = e.findAt(((       ((2*bb)+(k/2)+(2*bb)+k)/2, ((2*bb)-pp+2*bb)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=SINGLE, end2Edges=pickedEdges2, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER)
#h
pickedEdges = e.findAt(((      (k+(c/2)+(2*bb)+k)/2, (0.0+2*bb)/2, 0.0      ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)                           
# p
pickedEdges = e.findAt(((       (0.0+2*bb)/2, ((c/2)+2*bb)/2, 0.0          ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)
# m
pickedEdges = e.findAt(((       (k+(c/2)+(2*bb)+k+(c/2))/2, (0.0+2*bb-(c/2))/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)
# a
pickedEdges = e.findAt(((       (c/2)/2, (c/2)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)
# d
pickedEdges = e.findAt(((       ((2*bb)+k+(c/2)+(2*bb)+k)/2, (2*bb-(c/2)+2*bb)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh, constraint=FINER)

### arretes connexion x et y
pickedEdges = e.findAt(((       (c/2+(c/2)+k)/2, (0.0+0.0)/2, 0.0         ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER)
pickedEdges = e.findAt(((        (2*bb+2*bb+k)/2, (2*bb+2*bb)/2, 0.0           ),))
p.seedEdgeByBias(biasMethod=DOUBLE, endEdges=pickedEdges, minSize=minSizeMesh, maxSize=maxSizeMesh2, constraint=FINER)

#### elements constants sur partitions part et dautre des arrets x y
pickedEdges = e.findAt(((        (c/2-r+c/2+r)/2, (0.0+0.0)/2, 0.0           ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
pickedEdges = e.findAt(((       (c/2+k-r+c/2+k+r)/2, (0.0+0.0)/2, 0.0         ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
pickedEdges = e.findAt(((        (2*bb-r+2*bb+r)/2, (2*bb+2*bb)/2, 0.0           ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)                      
pickedEdges = e.findAt(((        (2*bb+k-r+2*bb+k+r)/2, (2*bb+2*bb)/2, 0.0           ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)                       

## elements constants sur les rdc
#c1
pickedEdges = e.findAt(((     2*bb-r, 2*bb-0.00001, 0.0        ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)    
#c2
pickedEdges = e.findAt(((        (c/2)+k+r, 0.00001, 0.0         ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c3
pickedEdges = e.findAt(((        (c/2)-r, 0.00001, 0.0          ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c4
pickedEdges = e.findAt(((       2*bb+k+r, 2*bb-0.00001, 0.0          ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
###c5
pickedEdges = e.findAt(((       2*bb+r*cos(atan ( pp/(k/2) )+alpha2),2*bb-r*sin(atan ( pp/(k/2) )+alpha2) , 0.0          ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
###c6
pickedEdges = e.findAt(((      2*bb+k-r*cos(atan ( pp/(k/2) )+alpha3)  ,2*bb-r*sin(atan ( pp/(k/2) )+alpha3) , 0.0         ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
###c7
pickedEdges = e.findAt(((       c/2+r*cos(alpha3+atan ( pp/(k/2) )) ,r*sin(alpha3+atan ( pp/(k/2) )),0.0     ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
###c8
pickedEdges = e.findAt(((      c/2+k-r*cos(alpha2+atan (pp/(k/2)))   ,r*sin(alpha2+atan ( pp/(k/2) )) , 0.0          ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c9
pickedEdges = e.findAt(((          (2*bb)+k+(c/2)-0.00001, 2*bb-(c/2)+r, 0.0          ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c10
pickedEdges = e.findAt(((          0.00001, (c/2)-r, 0.0                              ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c11
pickedEdges = e.findAt(((         (2*bb)+k+(c/2)-0.00001, 2*bb-(c/2)-r, 0.0           ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)
#c12 
pickedEdges = e.findAt(((          0.00001, (c/2)+r, 0.0                              ),))
p.seedEdgeBySize(edges=pickedEdges, size=minSizeMesh, deviationFactor=0.1,constraint=FINER)

###*******
elemType1 = mesh.ElemType(elemCode=elemcodtyp1, elemLibrary=STANDARD, # CPE4R lin / CPE8R quad
secondOrderAccuracy=OFF, hourglassControl=DEFAULT, 
distortionControl=DEFAULT)
elemType2 = mesh.ElemType(elemCode=elemcodtyp2, elemLibrary=STANDARD) # CPE3 lin / CPE6M quad
p = mdb.models['Pantographe'].parts['Part-1']
f = p.faces
faces = f.findAt(   (   (c/2, bb/4, 0.0),   )    )
pickedRegions =(faces, )
p.setElementType(regions=pickedRegions, elemTypes=(elemType1, elemType2))
pickedRegions = f.findAt(  ( (c/2, bb/4, 0.0), ))
p.setMeshControls(regions=pickedRegions, elemShape=forme)  
p = mdb.models['Pantographe'].parts['Part-1']
p.generateMesh()
cc = mdb.models['Pantographe']
t= cc.rootAssembly.instances['Part-1-1']

# referencepoint = (c/2 - r , 0 , 0)
referencepoint = (0 , 0 , 0)
Matrix1_C = isotrope2d(Young,Poisson)
MaterialSets_C={'Cellule':Matrix1_C}
Matrix2_C = isotrope2d_nsym(Young,Poisson)
NewMaterialSets_C = {'Cellule':Matrix2_C}
Matrix_S = isotrope2d_inverse(Young,Poisson)
MaterialSets_S={'Cellule':Matrix_S}
mdb.models[modelname].rootAssembly.Set(name='Set-1', vertices=t.vertices.findAt(((c/2 - r, 0.0, 0.0), )))