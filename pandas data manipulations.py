import pandas as pd
import numpy as np
'''data={
    'name':['ankita','pavin','kavita','raj'],
    'age':[20,30,40,10],
    'city':['dhule','mumbai','pune','nagpur']
}
df=pd.DataFrame(data)
print(df)
df.head()
df.info()
df.describe()

df=pd.DataFrame(data)
df['age_in_month']=df['age']*12
print(df)

filtered_df=df[df['age']<=30]
print(filtered_df)

sorted_df=df.sort_values(by='age')
print(sorted_df)

df.loc[2,'city']=np.nan
print(df)

df['city']=df['city'].fillna('unknown')
print(df)

df.to_csv('manipulated_data.csv',index=False)
print(df)'''

data_list=[10,40,60,22,30]
series_list=pd.Series(data_list,name='values')
print(series_list)

data_dict={'A':100,'B':200,'C':300}
series_dict=pd.Series(data_dict,name='score')
print(series_dict)

value_at_index_2=series_list[2]
print(value_at_index_2)

score_A=series_dict['A']
print(score_A)

series_list.loc[5]=67
print(series_list)

filtered_series=series_list[series_list>20]
print(filtered_series)

'''0    10
1    40
2    60
3    22
4    30
5    67'''

squered_series=series_list.apply(lambda x:x **2)
print(squered_series)

series_list.to_csv('series_list.csv',header=False)


delta=pd.Timedelta('1 day 2 hours 30 minutes')
print(delta)

now=pd.Timestamp.now()
print(now)
future=now+pd.Timedelta(days=10)
past=now-pd.Timedelta(hours=5)
print(future)
print(past)

deltas=pd.Series([pd.Timedelta('1 days'),pd.Timedelta('2 days')])
print(deltas)


date=pd.Series(pd.date_range('2024-11-22',periods=3))
shifted_dates=date+pd.Timedelta(days=5)
print(shifted_dates)

df=pd.DataFrame({
    'Event':['start','middle','end'],
    'Duration':[pd.Timedelta(hours=1),pd.Timedelta(hours=2),pd.Timedelta(hours=3)]
})
print(df)