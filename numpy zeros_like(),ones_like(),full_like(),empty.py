
#ones_like: Return an array of ones with shape and type of input.

Eg:Given the X numpy array, create a new numpy array with the same shape
and type as X, filled with ones

x=np.arange(4,dtype=int)
np.ones_like(x)

output: array([1, 1, 1, 1])   

#zeros_like: Return an array of zeros with shape and type of input.
Eg: X = np.array([[1,2,3], [4,5,6]], dtype=np.int)

np.zeros_like(X)

#full_like: Return a new array with shape of input filled with value.
Eg: X = np.array([[2,3], [6,2]], dtype=np.int)
    np.full_like(X,7)
    
output:     array([[7, 7],
                  [7, 7]])

#empty: Return a new uninitialized array.

