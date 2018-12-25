import tushare as ts
import pandas as pa
from pandas import Series, DataFrame
# ts.set_token('946d3a8d3e254c99aa5c8b502896fb79bdb97b5ad39d957fef21e8db')
# pro = ts.pro_api()
# print(pro)
# df = pro.daily(ts_code='000001.SZ', start_date='20181213', end_date='20181220')
# df.to_excel('testc.xlsx')
# df.to_json('b.json')
# print(df)

sd = {"python":8000,"c++":8100,"c#":4000}
print(sd)
print('----------1-----------')
s4 = Series(sd)
print(s4)

print('----------s5-----------')
s5 = Series(sd,index=['java','perl'])
print(s5)
print('----------s6-----------')
s6 = Series(sd,index=["java","python","c++","c#"])
print(s6)
print('----------s5 + s6-----------')
print(s5+s6)
print('----------5-----------')