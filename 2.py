# 2.二次元表作成

import csv

PREF_NUM = 48

with open('corona_base.txt','r',encoding='UTF-8') as rf:
    csvData = csv.reader(rf) # 取得したファイルオブジェクトを変数csvDataに格納
    allData = [aData for aData in csvData] # リスト内包表記

with open('corona_matrix.txt','w',newline='',encoding='UTF-8') as wf:
    writer = csv.writer(wf)

    ymdList = sorted(set([aData[0] for aData in allData[1:]])) # allDataの1行目から最終行までの各年月日(aData[0])を取得して重複を除いてソートしてリスト化
    ymdList.insert(0,'') # リストの最初に空のセルを挿入
    writer.writerow(ymdList) # 書き出し

    for n in range(2,PREF_NUM+1):
        write_data = [] # 書き込み用リストを毎行初期化
        write_data.append(allData[n][1]) # ALLと都道府県名の48個の項目名を行頭に順次挿入
        for aData in allData[n::PREF_NUM]:
            write_data.append(aData[2]) # ALLと都道府県名48個の項目名を行頭に入れたらその後に人数をカンマ区切りで挿入していく
        writer.writerow(write_data)