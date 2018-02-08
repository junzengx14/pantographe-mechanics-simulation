import numpy
def isotrope2d(Young,Poisson):
	lam = (Poisson * Young)/((1.0-2*Poisson)*(1.0+Poisson))
	mu = Young/(2*(1.0+Poisson))
	C_1111 = lam + 2*mu
	C_2222 = lam + 2*mu
	C_1122 = lam
	C_1212 = mu
	matrix_C = numpy.array(( (C_1111,C_1122,0.0),(C_1122,C_2222,0.0),(0.0,0.0,C_1212) ))
	return matrix_C

def isotrope2d_nsym(Young,Poisson):
	lam = (Poisson * Young)/((1.0-2*Poisson)*(1.0+Poisson))
	mu = Young/(2*(1.0+Poisson))
	C_1111 = lam + 2*mu
	C_2222 = lam + 2*mu
	C_1122 = lam
	C_1212 = mu
	matrix_C = numpy.array(( (C_1111,	0.0,	0.0,	C_1122),
							 (0.0,		C_1212,	C_1212,	0.0),
							 (0.0,		C_1212,	C_1212,	0.0),
							 (C_1122,	0.0,	0.0,	C_2222) ))
	return matrix_C

def isotrope2d_inverse(Young,Poisson):
	S_1111 = (1-Poisson**2)/Young
	S_2222 = (1-Poisson**2)/Young
	S_1122 = -(Poisson+Poisson**2)/Young
	S_1212 = (1+Poisson)/(2*Young)
	matrix_S = numpy.array(( (S_1111,	S_1122,	0.0   ),
							 (S_1122,	S_2222,	0.0   ),
							 (0.0,	    0.0,	4*S_1212) ))
	return matrix_S
 