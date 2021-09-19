# 3.月別二次元表作成

import datetime
import csv

def func_SUM_of_targetYearMonth(prefData):
    set_values_targetYearMonth = []
    values_targetYearMonthOfPref = [prefData[0][1],]
    for targetYearMonth in uniqueDate:
        set_values_targetYearMonth = []
        for a in prefData:
            if a[0][:7] == targetYearMonth:
                set_values_targetYearMonth.append(int(a[2]))
        values_targetYearMonthOfPref.append(sum(set_values_targetYearMonth))
    writer.writerow(values_targetYearMonthOfPref)

with open('corona_base.txt','r',encoding='UTF-8') as rf:
    csvData = csv.reader(rf) # 取得したファイルオブジェクトを変数csvDataに格納
    allData = [aData for aData in csvData] # リスト内包表記

with open('corona_monthly.txt','w',newline='',encoding='UTF-8') as wf:
    writer = csv.writer(wf)

    PREF_NUM = 48

    write_data = ['',] # 列名用に空白要素を行先頭に追加

    allDate = [aData[0][:7] for aData in allData] # aData[0] : 日付(ex.:2020/01/26)。aData[0][:7] : 日付の先頭から7文字目までを取得
    uniqueDate = sorted(set(allDate[1:])) # allDate[0]は項目名の行なので、allDate[1:]で取得。set関数で重複を取り除き、ソート。
    
    for a in uniqueDate:
        write_data.append(a)
    writer.writerow(write_data) # 年月を一行目に追加

    for n in range(2,PREF_NUM+1):
        prefData = [aData for aData in allData[n::PREF_NUM]]
        func_SUM_of_targetYearMonth(prefData)