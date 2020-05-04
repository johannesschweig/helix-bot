import random  # for random select
import json # to read joke file
import numpy as np
import pandas as pd

# jokes
# df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'])
# df2.to_csv('data/test.csv', index=False)
jokes = pd.read_csv('data/jokes.csv')
print(jokes)