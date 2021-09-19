# 4.月別千分率表作成

import csv

with open('corona_monthly.txt','r',encoding='UTF-8') as rf_corona_monthly:
    csvFile=csv.reader(rf_corona_monthly)
    allData_corona_monthly=[aData for aData in csvFile]

with open('population.csv','r',encoding='UTF-8') as rf_population:
    csvFile=csv.reader(rf_population)
    allData_population=[aData for aData in csvFile]

with open('corona_per_mille.txt','w',newline='',encoding='UTF-8') as wf:
    writer=csv.writer(wf)
    writer.writerow(allData_corona_monthly[0])

    for n in range(1,len(allData_corona_monthly)):
        for m in range(1,len(allData_corona_monthly[0])):
            allData_corona_monthly[n][m]=round(int(allData_corona_monthly[n][m])/int(allData_population[n-1][1]),1)
        writer.writerow(allData_corona_monthly[n])