# Series        -  1D
# Dataframes    -  2D
# Panel         -  More than 2D

import pandas as pd
import numpy as np

data = np.array(['Baahubali',
        'Fukrey',
        'Tubelight',
        'Singham',
        'ABCD',
        'ABCD2',
        'Race',
        'Race2',
        'Dabang',
        'Dabang2'])

s = pd.Series(data)
print(s)

# Head - first 5 observations
s.head()

# Tail - last 5 observations
s.tail()








