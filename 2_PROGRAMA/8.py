#8. Sukurkite atsitiktini masyva dydzio 5x5 naudodami np.random.rand(5, 5). 
# Surusiuokite eilutes pagal antraji stulpeli. 
# Tam pameginkite apjungti masyvo slicing + argsort + indexing metodus.

import numpy as np
m = np.random.rand(5, 5)


print(m)
print(m[np.argsort(m[:,1])])