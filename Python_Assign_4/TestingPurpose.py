import pandas as pd
import numpy as np

dff = pd.DataFrame(np.random.randn(100,3),columns=list('ABC'))
print(dff)
print("Mean of the data column wise=\n",dff.mean(axis=1))