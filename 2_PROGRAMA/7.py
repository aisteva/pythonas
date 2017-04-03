#7.Sukurkite atsitiktini masyva dydzio 3x5 naudodami
#np.random.rand(3, 5) funkcija ir suskaiciuokite:
#suma, eiluciu suma, stulpeliu suma.
#array1 = np.arange(9).reshape([3,3])

import numpy as np
array = np.random.rand(3, 5)


sumAll = array.sum()
sumColumn = sum(array)
sumRow = array.sum(axis=1)


print(array)
print("Bendra suma", sumAll)
print("Stulpeniu sumos", sumColumn)
print("Eiluciu suma", sumRow)
