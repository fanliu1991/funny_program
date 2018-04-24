'''
Exercise for Python NumPy
'''
# import sys, optparse, os
import numpy as np

# 1. Generate five random numbers from the normal distribution
def fun1():
    x = np.random.normal(size=5)
    print x

# 2. generate six random integers between 10 and 30
def fun2():
    x = np.random.randint(low=10, high=30, size=6)
    print x

# 3. create a 3x3x3 array with random values
def fun3():
    x = np.random.random((3,3,3))
    print x

# 4. create a 5x5 array with random values and find the minimum and maximum values
def func4():
    x = np.random.random((5,5))
    print x
    xmin, xmax = x.min(), x.max()
    print "minimum = ", xmin, "maximum = ", xmax

# 5. create a random 10x4 array and extract the first five rows of the array and store them into a variable
def fun5():
    x = np.random.rand(10, 4) # same as np.random.random((10,4))
    print x
    y = x[:5, :]
    print "the first five rows are ", "\n", y

# 6. shuffle numbers between 0 and 10 (inclusive)
def fun6():
    x = np.arange(10) # [0 1 2 3 4 5 6 7 8 9]
    np.random.shuffle(x) # same as np.random.permutation(10)
    print x

# 7. normalize a 3x3 random matrix
def fun7():
    x = np.random.random((3,3))
    print "Original Array: \n", x
    xmax, xmin = x.max(), x.min()
    x = (x - xmin)/(xmax - xmin)
    print "After normalization: \n", x

# 8. create a random vector of size 10 and sort it
def fun8():
    x = np.random.random(10)
    x.sort()
    print x

# 9. find the nearest value from a given value in an array
def fun9():
    x = np.random.uniform(1, 12, 5)
    v = 4
    n = x.flat[np.abs(x - v).argmin()] # same as x[np.abs(x - v).argmin()]
    # numpy.argmin(a, axis=None, out=None)
    # returns the indices of the minimum values along an axis
    print x
    print np.abs(x - v).argmin()
    print n

# 10. check two random arrays are equal or not
def fun10():
    x = np.random.randint(0,2,6)
    y = np.random.randint(0,2,6)
    array_equal = np.allclose(x, y)
    # numpy.allclose(a, b, rtol=1e-05, atol=1e-08, equal_nan=False)[source]
    # returns True if two arrays are element-wise equal within a tolerance.
    print array_equal

# 11. create random vector of size 15 and replace the maximum value by -1
def fun11():
    x = np.random.random(15)
    x[x.argmax()] = -1
    print x

# 12. find point by point distances of a random vector with shape (10,2) representing coordinates
def fun12():
    a = np.random.random((10,2))
    x, y = np.atleast_2d(a[:,0], a[:,1])
    # numpy.atleast_2d(*arys)
    # view inputs as arrays with at least two dimensions.
    d = np.sqrt( (x-x.T)**2 + (y-y.T)**2)
    print "coordinates x: ", x, "\n", "coordinates x transpose: ", x.T
    print(d)

# 13. find the most frequent value in an array
def fun13():
    x = np.random.randint(0, 10, 40)
    numbers = list(set(x))
    numbers.sort()
    freq = np.bincount(x).argmax()
    # numpy.bincount(x, weights=None, minlength=0)
    # count number of occurrences of each value in array of non-negative ints.
    # the number of bins (of size 1) is one larger than the largest value in x, e.g. largest number in x = 7, return array of 8 elements
    print x
    print "above list without duplication:", numbers
    print "frequence count:", np.bincount(x), "most frequent number:", freq

# 14. convert cartesian coordinates to polar coordinates of a random 10x3 matrix representing cartesian coordinates
def fun14():
    z = np.random.random((10, 3))
    x, y = z[:,0], z[:,1]
    distance = np.sqrt(x**2+y**2)
    angle = np.arctan2(y, x) * 180 / np.pi
    print zip(distance, angle)

# 15. find the closest value (to a given scalar) in an array
def fun15():
    x = np.arange(100)
    print "Original array:"
    print x
    a = np.random.uniform(0,100)
    print "Value to compare:"
    print a
    index = (np.abs(x-a)).argmin()
    print x[index]

# 16. get the n largest values of an array
def fun16():
    x = np.arange(10, 25)
    np.random.shuffle(x)
    sorted_index = np.argsort(x)
    # numpy.argsort(a, axis=-1, kind='quicksort', order=None)
    # returns the indices that would sort an array
    n = 3
    result = x[sorted_index[-n]]
    print x
    print sorted_index
    print x[sorted_index]
    print result


if __name__ == "__main__":
    fun16()

