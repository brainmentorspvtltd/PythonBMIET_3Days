# Series        -  1D
# Dataframes    -  2D
# Panel         -  More than 2D

import pandas as pd
import numpy as np

names = np.array(['Baahubali',
        'Fukrey',
        'Tubelight',
        'Singham',
        'ABCD',
        'ABCD2',
        'Race',
        'Race2',
        'Dabang',
        'Dabang2'])
ratings = np.array([4,5,4,None,2,4,None,5,3,4])


data = {
    'movie_name' : names,
    'ratings' : ratings    
    }

df = pd.DataFrame(data)
print(df)








