#12. Pasirinktos funkcijos apibreztini ir neapibreztini integralus

from scipy.integrate import quad
import numpy

def f(x):
    return x**2

ats1, e1 = quad(f, 0, 2)
ats2, e2 = quad(f, -numpy.inf, +numpy.inf)


print("Apibreztinis integralas:  ", ats1)
print("Neapibreztinis integralas:  ", ats2)

