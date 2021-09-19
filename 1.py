# 1.基本データ作成

import csv
import prefList

with open('newly_confirmed_cases_daily.csv','r',encoding='UTF-8') as rf:
    csvData = csv.reader(rf) # 取得したファイルオブジェクトを変数csvDataに格納
    allData = [aData for aData in csvData] # リスト内包表記

with open('corona_base.txt','w',newline='',encoding='UTF-8') as wf:
    writer = csv.writer(wf)

    write_data = ['日付','都道府県名','人数']
    writer.writerow(write_data) # 1行目に「日付,都道府県名,人数」を追記

    for aData in allData[1:]:                # CSVファイルの2行目から1行ずつ走査してaDataに格納する
                                             # aData[0] : 日付
                                             # aData[1] : 都道府県名
                                             # aData[2] : 人数
        write_data = [] # write_dataを初期化
        y,m,d = aData[0].split('/') # aData[0]に格納されている日付(ex.:2020/1/26)をaDateに格納する
        aDate=f'{y}/{int(m):02d}/{int(d):02d}' # yyyy/mm/dd表記でaDateに格納
        write_data.append(aDate)
        pref = prefList.converter[aData[1]] # ローマ字表記の都道府県名を漢字表記にする
        write_data.append(pref)
        write_data.append(aData[2]) # 人数を追加
        writer.writerow(write_data) # ['yyyy/mm/dd','都道府県名','人数']を1行ずつ追記