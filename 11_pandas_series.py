# Create a Pandas Series with ten random numbers
import pandas as pd
import numpy as np

random_numbers = np.random.randint(1, 101, size=10)
series = pd.Series(random_numbers)
print("Pandas Series:")
print(series)
