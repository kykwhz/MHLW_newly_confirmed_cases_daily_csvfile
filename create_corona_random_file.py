# corona_base.txtについて、
# 感染者数が0人の日は削除して、
# 全体のリストをランダムに並び替えて、
# corona_random.txtに出力する。

import csv
import random

with open('corona_base.txt','r',encoding='UTF-8') as rf:
    rf_csvFile=csv.reader(rf)
    allData=[aData for aData in rf_csvFile]

with open('corona_random.txt','w',newline='',encoding='UTF-8') as wf:
    wf_csvFile=csv.writer(wf)

    wf_csvFile.writerow(allData[0]) # 項目名を一行目に書き出し
    not_Zero_value_list = list(filter(lambda aData:aData[2]!='0',allData[1:])) # 感染者数が0でない行だけでリスト化
    random.shuffle(not_Zero_value_list) # シャッフル
    [wf_csvFile.writerow(aData) for aData in not_Zero_value_list] # 書き出し