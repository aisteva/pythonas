# 5. Sukurkite masyva dydzio 8 x 8, 
# kur 1 ir 0 isdelioti sachmatine tvarka (panaudokite slicing+striding metoda).

import numpy as np

a = np.zeros((8,8), int)
a[1:8:2,::2] = 1
a[::2,1:8:2] = 1


print(a)