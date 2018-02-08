import time
m = mdb.models[modelname]
m.Stress(name = 'prestress',distributionType=USER_DEFINED, region=t.sets['Cellule'])
for ind,charge in enumerate(Charge):
    del m.steps['Step-'+charge]
mdb.models[modelname].PinnedBC(createStepName='Initial', localCsys=None, 
    name='BC-25', region=mdb.models[modelname].rootAssembly.sets['Set-1'])

############ BCs ################
#STEP-K111
m.StaticStep(name='Step-K111',previous= 'Initial')
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K111', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-1', region=t.sets['droite'], 
u1= UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K111'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-2', region=t.sets['bas'],
 u1=UNSET,u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K111'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-3', region=t.sets['gauche'], 
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K111'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-4', region=t.sets['haut'],
u1=UNSET, u2=0.0, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K111', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K111', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K111', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K1', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K1'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K1'].waitForCompletion()
m.steps['Step-K111'].suppress()

#STEP-K221
m.StaticStep(name='Step-K221',previous= 'Initial')
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K221', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-5', region=t.sets['droite'], 
u1= UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K221'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-6', region=t.sets['bas'],
u1=UNSET,u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K221'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-7', region=t.sets['gauche'], 
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K221'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-8', region=t.sets['haut'],
u1=UNSET, u2=0.0, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K221', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K221', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K221', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K2', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K2'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K2'].waitForCompletion()
m.steps['Step-K221'].suppress()

#STEP-K121
m.StaticStep(name='Step-K121',previous= 'Initial')
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K121', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-13', region=t.sets['droite'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K121'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-14', region=t.sets['bas'],
 u1=0.0,u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K121'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-15', region=t.sets['gauche'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K121'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-16', region=t.sets['haut'],
u1=0.0, u2=UNSET, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K121', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K121', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K121', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K3', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K3'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K3'].waitForCompletion()
m.steps['Step-K121'].suppress()

#STEP-K112
m.StaticStep(name='Step-K112',previous= 'Initial')
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K112', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-17', region=t.sets['droite'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K112'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-18', region=t.sets['bas'],
 u1=0.0,u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K112'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-19', region=t.sets['gauche'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K112'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-20', region=t.sets['haut'],
u1=0.0, u2=UNSET, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K112', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K112', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K112', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K4', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K4'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K4'].waitForCompletion()
m.steps['Step-K112'].suppress()

#STEP-K222
m.StaticStep(name='Step-K222',previous= 'Initial') 
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K222', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-21', region=t.sets['droite'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K222'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-22', region=t.sets['bas'],
u1=0.0,u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K222'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-23', region=t.sets['gauche'], 
u1=0.0, u2=UNSET, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K222'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-24', region=t.sets['haut'],
u1=0.0, u2=UNSET, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K222', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K222', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K222', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K5', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K5'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K5'].waitForCompletion()
m.steps['Step-K222'].suppress()

#STEP-K122
m.StaticStep(name='Step-K122',previous= 'Initial')
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K122', 
    distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-9', region=t.sets['droite'], 
u1= UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K122'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-10', region=t.sets['bas'],
 u1=UNSET,u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K122'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-11', region=t.sets['gauche'], 
u1=UNSET, u2=0.0, ur3=UNSET)
cc.DisplacementBC(amplitude=UNSET, createStepName='Step-K122'
    , distributionType=UNIFORM, fieldName='', fixed=OFF, localCsys=None, name='BC-12', region=t.sets['haut'],
u1=UNSET, u2=0.0, ur3=UNSET)
m.FieldOutputRequest(createStepName='Step-K122', name='F-Output-2', variables=('S', 'E', 'U' , 'IVOL','EVOL','BF'))
m.HistoryOutputRequest(createStepName='Step-K122', name='H-Output-2', variables=PRESELECT)
m.BodyForce(comp1=1.0, comp2=1.0, comp3=1.0, 
                 createStepName='Step-K122', distributionType=USER_DEFINED, field='', name=
                 charge+'BodyForce', region=t.sets['Cellule'])
mdb.Job(atTime=None, contactPrint=OFF, description='', echoPrint=OFF, 
    explicitPrecision=SINGLE, getMemoryFromAnalysis=True, historyPrint=OFF, 
    memory=90, memoryUnits=PERCENTAGE, model=modelname, modelPrint=OFF, 
    multiprocessingMode=DEFAULT, name='Job_ordre_2_K6', nodalOutputPrecision=SINGLE, 
    numCpus=1, numGPUs=0, queue=None, scratch='', type=ANALYSIS, 
    userSubroutine='DLOAD_SIGINI.for', waitHours=0, waitMinutes=0)
mdb.jobs['Job_ordre_2_K6'].submit(consistencyChecking=OFF)
mdb.jobs['Job_ordre_2_K6'].waitForCompletion()
m.steps['Step-K122'].suppress()
