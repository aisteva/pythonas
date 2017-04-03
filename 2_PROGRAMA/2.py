# 2. Sugeneruokite masyva dydzio 3n ir uzpildykite ji cikliniu sablonu [1, 2, 3].

import numpy as np
x = [1 ,2, 3]
n = 3
array = np.array(x)
result = np.tile(array, n)

print(result)