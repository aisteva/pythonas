#4. Sukurkite masyva dydzio 10 x 10 iz nuliu ir "ireminkite" ji vienetais.

import numpy as np

array = np.zeros((10,10), int)
array[0,] = 1
array[9,] = 1
array[...,0] = 1
array[...,9] = 1
print(array)




