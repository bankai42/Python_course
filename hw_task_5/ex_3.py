import pandas as pd
import numpy as np
import string as s


#Exersize 3
mat = np.random.randint(1,10,size=(10,10))
df = pd.DataFrame(mat)
new_cols = dict(map(lambda i,j: (i,j), df.columns.values, list(s.ascii_lowercase)[:10]))
df.rename(new_cols, axis=1, inplace=True)
print(df)