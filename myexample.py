import pandas as pd

import numpy as np

mat = np.arange(0, 10).reshape(5, 2)
df = pd.DataFrame(data=mat, columns=['A', 'B'])
print(df)
