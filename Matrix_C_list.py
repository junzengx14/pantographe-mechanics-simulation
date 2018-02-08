# material and sets association's Matrix_C
Matrix_C = numpy.zeros((noe,3,3)) # 3 * 3 at integration points

for surface in MaterialSets_C.keys():
    matrix = MaterialSets_C[surface]
    elements_list_temp = p.sets[surface].elements
    for j in range(len(elements_list_temp)):
        label = elements_list_temp[j].label - 1
        Matrix_C[label,:,:] = matrix

Matrix_C_new = numpy.zeros((noip,4,4))  # 4 * 4 at integration points
# new matrix is 4 * 4 and in each bloc we will use partially of it during the multiplication
for surface in NewMaterialSets_C.keys():
    matrix = NewMaterialSets_C[surface]
    elements_list_temp = p.sets[surface].elements
    for i in range(len(elements_list_temp)):
        label = elements_list_temp[i].label - 1
        for j in range(4):
        	Matrix_C_new[4*label+j,:,:] = matrix

Matrix_S = numpy.zeros((noip,3,3))

for surface in MaterialSets_S.keys():
    matrix = MaterialSets_S[surface]
    elements_list_temp = p.sets[surface].elements
    for i in range(len(elements_list_temp)):
        label = elements_list_temp[i].label - 1
        for j in range(4):
            Matrix_S[4*label+j,:,:] = matrix