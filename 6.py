# 6.曜日算出

import datetime

date_string=input(f'日付を入力してください(入力形式は2021-01-01) >>> ')
try:
    date=datetime.date.fromisoformat(date_string)
    y=date.year
    m=date.month
    d=date.day
    a=date.weekday()

    weekday={0:'月',1:'火',2:'水',3:'木',4:'金',5:'土',6:'日'}

    print(f'{y}/{m}/{d}({weekday[a]})')
except:
    print(f'日付不当')