import time
# from scipy.io import FortranFile
from MyFortranfile import FortranFile
#unf format storage
Charge = ['E11','E22','E12']

force11 = FortranFile('force11.unf', 'w')
force12 = FortranFile('force12.unf', 'w')
force13 = FortranFile('force13.unf', 'w')
force14 = FortranFile('force14.unf', 'w')
force15 = FortranFile('force15.unf', 'w')
force16 = FortranFile('force16.unf', 'w')
force21 = FortranFile('force21.unf', 'w')
force22 = FortranFile('force22.unf', 'w')
force23 = FortranFile('force23.unf', 'w')
force24 = FortranFile('force24.unf', 'w')
force25 = FortranFile('force25.unf', 'w')
force26 = FortranFile('force26.unf', 'w')

with file('S24.txt', 'w') as outfile_FORCE24:
# f plutot que s... correspond a la notation de Voigt [2x6]
    for k in xrange(noip):
    #STEP E11
        force11.write_record(numpy.float32(S[k,0,0]-(l1*l2/area)*Stiffness[0,0]))
        # numpy.savetxt(outfile_FORCE11,  array(S[k,0,0]-Stiffness[0,0]).reshape(1,), fmt='%-7.8E')
        force24.write_record(numpy.float32(S[k,0,1]-(l1*l2/area)*Stiffness[0,1]))
        force21.write_record(numpy.float32(S[k,0,3]))
        # numpy.savetxt(outfile_FORCE24,  array().reshape(1,), fmt='%-7.8E')
        force14.write_record(numpy.float32(S[k,0,3]))
    #STEP E22   
        force12.write_record(numpy.float32(S[k,1,0]-(l1*l2/area)*Stiffness[0,1]))
        force25.write_record(numpy.float32(S[k,1,1]-(l1*l2/area)*Stiffness[1,1]))
        force22.write_record(numpy.float32(S[k,1,3]))
        force15.write_record(numpy.float32(S[k,1,3]))
    #STEP E12   
        force13.write_record(numpy.float32(S[k,2,0]))
        force26.write_record(numpy.float32(S[k,2,1]))
        force23.write_record(numpy.float32(S[k,2,3]-(l1*l2/area)*Stiffness[2,2]/sqrt(2)))
        force16.write_record(numpy.float32(S[k,2,3]-(l1*l2/area)*Stiffness[2,2]/sqrt(2)))
force11.close()
force12.close()
force13.close()
force14.close()
force15.close()
force16.close()
force21.close()
force22.close()
force23.close()
force24.close()
force25.close()
force26.close()