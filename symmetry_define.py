def symmetry_null_6_6(matrix):
	matrix[2:5,0:2] = 0
	matrix[0:2,2:5] = 0
	matrix[2:5,5] = 0
	matrix[5,2:5] = 0
	
	return matrix
def symmetry_null_12_12(matrix):
	# Bloc 11
	matrix[2:5,0:2] = 0
	matrix[0:2,2:5] = 0
	matrix[2:5,5] = 0
	matrix[5,2:5] = 0
	# Bloc 12
	matrix[0:2,6:8] = 0
	matrix[2:5,8:11] = 0
	matrix[5,0:8] = 0
	matrix[0:2,11] = 0
	matrix[5,11] = 0
	# Bloc 21
	matrix[6:8,0:2] = 0
	matrix[8:11,2:5] = 0
	matrix[11,0:2] = 0
	matrix[6:8,5] = 0
	matrix[11,5] = 0
	# Bloc 22
	matrix[8:11,6:8] = 0
	matrix[6:8,8:11] = 0
	matrix[8:11,11] = 0
	matrix[11,8:11] = 0

	return matrix


