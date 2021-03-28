import numpy
import numba
from tqdm import tqdm

@numba.njit([
    'float64[:](float64[:,:])'
], cache=True)
def anorm2(X):
	return numpy.sqrt(numpy.sum(X ** 2, axis = 1))


@numba.njit([
    'float64[:](float64[:,:],float64[:,:], float64[:,:])'
], cache=True)
def adet(X, Y, Z):
	ret  = numpy.multiply(numpy.multiply(X[:,0], Y[:,1]), Z[:,2])
	ret += numpy.multiply(numpy.multiply(Y[:,0], Z[:,1]), X[:,2])
	ret += numpy.multiply(numpy.multiply(Z[:,0], X[:,1]), Y[:,2])
	ret -= numpy.multiply(numpy.multiply(Z[:,0], Y[:,1]), X[:,2])
	ret -= numpy.multiply(numpy.multiply(Y[:,0], X[:,1]), Z[:,2])
	ret -= numpy.multiply(numpy.multiply(X[:,0], Z[:,1]), Y[:,2])
	return ret


#@numba.njit([
#    'b1[:](float64[:,:,:], float64[:,:])',
#    'b1[:](float32[:,:,:], float32[:,:])',
#    'b1[:](float32[:,:,:], float64[:,:])',
#    'b1[:](float64[:,:,:], float32[:,:])',
#])
def is_inside_turbo(triangles, X):

	# One generalized winding number per input vertex
	ret = numpy.zeros(X.shape[0], dtype = X.dtype)
	
	# Accumulate generalized winding number for each triangle
	for U, V, W in tqdm(triangles, desc='Preprocessing'):	
		A, B, C = U - X, V - X, W - X
		omega = adet(A, B, C)

		a, b, c = anorm2(A), anorm2(B), anorm2(C)
		k  = a * b * c 
		k += c * numpy.sum(numpy.multiply(A, B), axis = 1)
		k += a * numpy.sum(numpy.multiply(B, C), axis = 1)
		k += b * numpy.sum(numpy.multiply(C, A), axis = 1)

		ret += numpy.arctan2(omega, k)

	# Job done
	return ret >= 2 * numpy.pi 