# 5.ランダムデータからの二次元表作成

import csv
from os import write
import prefList

PREF_NUM=48

with open('corona_random.txt','r',encoding='UTF-8') as rf:
    rf_csvFile=csv.reader(rf)
    allData=[aData for aData in rf_csvFile]

with open('randomed_matrix.txt','w',newline='',encoding='UTF-8') as wf:
    wf_csvFile=csv.writer(wf)

    unique_date=sorted(set([aData[0] for aData in allData[1:]])) # 日付の重複を除いてリスト化し昇順に並び替え
    unique_date.insert(0,'') # 先頭に空セルを追加
    wf_csvFile.writerow(unique_date) # 一行目を書き込み

    for n in range(1,PREF_NUM):
        write_data=[prefList.converter_list[n],] # 各行の先頭に都道府県名を記入
        pref_allData=list(filter(lambda aData:aData[1]==prefList.converter_list[n],[aData for aData in allData]))
        for m in range(1,len(unique_date)):
            pref_unique_date_aData=[aData[2] for aData in filter(lambda aData : aData[2] if aData[0]==unique_date[m] else '',pref_allData)]
            if pref_unique_date_aData == []:
                write_data.append('')
            else:
                write_data.append(pref_unique_date_aData[0])
        wf_csvFile.writerow(write_data)