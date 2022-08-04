import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(2))
print(s)
print(s.size)

print(80*'*')
p = [[1,0], [0,1]]
q = [[1,2], [3,4]]

r1= np.cross(p, q)
r2 = np.cross(q,p)
print(r1)
print(r2)
print(r1==r2)
print((r1==r2).shape[0])