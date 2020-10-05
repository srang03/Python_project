import pandas as pd
import matplotlib.pyplot as plt

# print(drive_report.loc['대한민국','2014'])
# print(drive_report.loc['핀란드','2014'])

# print(drive_report.loc['미국':'프랑스','2014':'2015'])

drive_report = pd.read_csv('./data_file/Report.csv',index_col='국가', encoding='cp949')
oecd_top = drive_report.loc['대한민국':'스웨덴']
print(oecd_top)
def draw_graph(drive_report):

    plt.rc('font', family='NanumBarunGothic')

    drive_report.plot(kind='bar', rot=0,
    title="대한민국, 스페인, 스웨덴 교통사고 사망자 수")
    # plt.legend(loc=5)

    plt.savefig('drive_graph.png')



draw_graph(oecd_top)

