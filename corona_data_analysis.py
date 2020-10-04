import pandas as pd

corona_data = pd.read_excel('./data_file/corona_data_.xlsx', index_col=0)
print(corona_data.columns)

print(corona_data)