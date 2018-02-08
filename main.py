import numpy
import timeit
from MyFortranfile import FortranFile
from Matrix_C import *
from symmetry_define import *
global Stiffness 
global D_hom
r = 0.001
modelname = 'Pantographe'
execfile(modelname+'.py')
execfile('ordre_1.py')
execfile('Post_Traitement_ordre_1.py')
execfile('C_hom_calculation.py')
execfile('Matrix_C_list.py')
execfile('Precontrainte_Storage.py')
execfile('integrationpoints_force_storage.py')
execfile('D_calculation.py')
execfile('ordre_2.py')
execfile('Post_Traitement_ordre_2.py')
execfile('F_calculation.py')
execfile('G_calculation.py')
execfile('affichage.py')
stop = timeit.default_timer()
print stop - start
  

