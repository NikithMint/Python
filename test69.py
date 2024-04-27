import pandas as pd
row_arrays = ['USA', 'USA', 'Mexico', 'Mexico', 'Canada', 'Canada']
col_arrays = [1990, 2000, 1990, 2000, 1990, 2000]
multi_index = pd.MultiIndex.from_arrays([row_arrays,col_arrays],names=('Country','Year'))
print(multi_index)
