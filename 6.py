# 6.曜日算出

import datetime

y,m,d=input(f'日付を入力してください(入力形式は2021-01-01,2021-1-1両方可) >>> ').split('-')
date_string=f'{int(y)}-{int(m):02d}-{int(d):02d}'

try:
    date=datetime.date.fromisoformat(date_string) # date_stringに格納されている入力年月日が妥当でなければexceptで処理
    weekday={0:'月',1:'火',2:'水',3:'木',4:'金',5:'土',6:'日'}
    print(f'{date.year}/{date.month}/{date.day}({weekday[date.weekday()]})')
except:
    print(f'日付不当')