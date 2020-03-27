import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
# da = np.random.randint(1, 5, size=(7))
# print(da)
# print(np.unique(da))
# d = pd.Series(da, index=None)

# da = pd.Series([1, 2, np.nan, np.nan])
# print(da[da.notnull()].values)

p = np.random.randn(5, 3)
d = PCA(n_components=2)
d.fit(p)
print()
print(d.transform(p))
