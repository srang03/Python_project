import pandas as pd

corona_data = pd.read_excel('./data_file/corona_data_.xlsx', index_col="날짜")
print(corona_data.columns)

# 2020-03-03 코로나 누적검사 수
print(corona_data.loc['2020-03-03','누적검사'])

# 2020-03-03 코로나 사망자 수
print('사망자는 {}명 입니다.'.format(corona_data.loc['2020-03-03','사망자']))

print(corona_data.loc['2020-03-03','확진자'])

# 2020 3월 코로나 확진자 수
print(corona_data.loc['2020-03-01:2020-03-31','확진자'])

print(corona_data)