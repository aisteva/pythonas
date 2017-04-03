#6. Sukurkite masyva dydzio nxn , kurio (i,j)-oji pozicija lygi i+j

import numpy as np

n = 4

a = np.fromfunction(lambda i, j: i + j, (n, n), dtype=int)

print(a)