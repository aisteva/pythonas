# Arvirsktine matrica

import numpy as np

a = np.array([(1,4), (-3,9)])
print("Matrica: \n", a)

inverse = np.linalg.inv(a)

print("Atvirkstine matrica: \n", inverse)
