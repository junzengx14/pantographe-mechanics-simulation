############### 4 STEP  ############
m.StaticLinearPerturbationStep(name='Step-E11',previous= 'Initial')
m.StaticLinearPerturbationStep(name='Step-E22',previous='Step-E11')
m.StaticLinearPerturbationStep(name='Step-E12',previous= 'Step-E22')
m.fieldOutputRequests['F-Output-1'].setValues(variables=('S', 'E', 'U' , 'IVOL','EVOL'))
m.historyOutputRequests['H-Output-1'].setValues(variables=('ALLSE', ))
                                                           
############ BCs ################
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E11', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-1', region=t.sets['droite'], 
u1= l1, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E11'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-2', region=t.sets['bas'],
 u1=UNSET,u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E11'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-3', region=t.sets['gauche'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E11'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-4', region=t.sets['haut'],
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E22'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-5', region=t.sets['droite'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E22'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-6', region=t.sets['bas']  , 
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E22'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-7', region=t.sets['gauche'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E22'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-8', region=t.sets['haut'], 
u1=UNSET, u2=l2, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E12'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-13', region=t.sets['droite'], 
u1=UNSET, u2=l1/sqrt(2), ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E12'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-14', region=t.sets['bas'], u1=0.0, 
u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E12'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-15', region=t.sets['gauche'], 
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-E12'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-16', region=t.sets['haut'], 
u1=l2/sqrt(2), u2=UNSET, ur3=UNSET)

mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_1'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_1'].waitForCompletion()