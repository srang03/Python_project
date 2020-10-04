import pandas as pd

corona_data = pd.read_excel('./data_file/corona_data_.xlsx', index_col="날짜")
print(corona_data.columns)

print(corona_data['격리해제'])
print(corona_data['확진자'])

print(corona_data)