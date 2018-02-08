numpy.savetxt(str(r)+'_C.csv',Stiffness,delimiter=';')
D = symmetry_null_6_6(D)
print('D',D,)
numpy.savetxt(str(r)+'_D.csv',D,delimiter=';')
F = symmetry_null_6_6(F)
print('F',F)
numpy.savetxt(str(r)+'_F.csv',F,delimiter=';')
G = symmetry_null_6_6(G)
print('G',G)
numpy.savetxt(str(r)+'_G.csv',G,delimiter=';')
J = F - G.transpose() - G
print('J',J) 
numpy.savetxt(str(r)+'_J.csv',J,delimiter=';')
LL = (J[4,4]/Stiffness[1,1])**(0.5)
results_list.append(LL)

os.remove('Job_ordre_1.lck')
for i in range(6):
	os.remove('Job_ordre_2_K'+str(i+1)+'.lck') 
openOdb('Job_ordre_1.odb').close()
for i in range(6):
	openOdb('Job_ordre_2_K'+str(i+1)+'.odb').close()