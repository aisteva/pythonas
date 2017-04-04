#12. Pasirinktos funkcijos apibreztini ir neapibreztini integralus

from scipy.integrate import quad
import numpy as np

def f(x):
    return x**2

ats1, e1 = quad(f, 0, 2)
p = np.poly1d([1,0,0])
ats2 = np.polyint(p)


print("Apibreztinis integralas:  ", ats1)
print("Neapibreztinis integralas:  \n", ats2)

