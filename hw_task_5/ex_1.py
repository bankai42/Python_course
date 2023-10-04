import pandas as pd
import numpy as np
import string as s

# Exersize 1
mat = np.random.randint(1,10,size=(10,10))
df = pd.DataFrame(mat)
print(df)
print(mat)

# Exersize 2
new_index = dict(map(lambda i,j: (i,j), df.index.values, list(s.ascii_lowercase)[:10]))
df.rename(new_index, inplace=True)
print(df)
print('\n\n\n')
print(df[df.columns > 5])

