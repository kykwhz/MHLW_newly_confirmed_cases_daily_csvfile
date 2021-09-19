# 6.曜日算出

import datetime
import re
y,m,d=re.split('[/-]',input(f'日付を入力してください(入力形式は2021-01-01,2021-1-1,両方可。区切り文字は/,-両方可) >>> '))

try:
    date=datetime.date(int(y),int(m),int(d)) # date_stringに格納されている入力年月日が妥当でなければexceptで処理
    weekday={0:'月',1:'火',2:'水',3:'木',4:'金',5:'土',6:'日'} # 曜日変換ディクショナリ
    print(f'{date.year}/{date.month}/{date.day}({weekday[date.weekday()]})')
except:
    print(f'日付不当')