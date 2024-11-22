import numpy as np
import pandas as pd
data={
    'Name':['Ankita','raj','kavita','pravin'],
    'Age':[30,40,50,60],
    'City':['mumbai','pune','mumbai','pune']
}
df=pd.DataFrame(data)
print(df)

count_non_null=df.count()
print(count_non_null)

description=df.describe(include='all')
print(description)

df_drop_duplicate=df.drop_duplicates()
print(df_drop_duplicate)

is_empty=df.empty
print(is_empty)

filtered=df[df['City']=='mumbai']
print(filtered)

df_copy=df.copy()
df_equal=df.equals(df_copy)
print(df_equal)