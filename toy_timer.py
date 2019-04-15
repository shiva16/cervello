import numpy as np

d = {}

key_l = []
for i in range(12870):
    key = np.random.randint(100000000,1000000000)
    if np.random.uniform(0,1) < 0.1:
        key_l.append(key)
    d[key] = np.random.random(size=10000)

import time

start = time.time()
for k in key_l:
    r = d[k]
end = time.time()
print((end-start)/len(key_l), len(key_l))
