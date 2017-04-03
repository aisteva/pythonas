

from scipy.misc import derivative
def f(x):
	return 2*x + x**2
d = derivative(f, 1)

print(d)
