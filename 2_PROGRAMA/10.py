#10. Apskaiciuokite matricos tikrines reiksmes ir tikrini vektoriu

import numpy as np
import numpy.linalg as la

m = np.random.random((3,3))

values, vectors = la.eig(m)

print("Matrica: \n", m)
print("Tikrines reiksmes: \n", values)
print("Tikriniai vektoriai: \n", vectors)