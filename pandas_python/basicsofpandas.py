import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')
data={
    "Name":["Alicy","Rocky", "Charlie", "nelson"],
    "Age":[12,34,45,np.nan],
    "City":["new york","London",None,None]
}

print(data)
df=pd.DataFrame(data)
print(df)

print(type(df))
print(df.head(2))

print(df.isnull())

# df=df.fillna("No data")
print(df)

data={
    "Name":["Alicy","Rocky", "Charlie", "nelson"],
    "Age":[12,34,45,None],
    "City":["new york","London",None,None]
}
df["Age"] = df["Age"].fillna(df["Age"].mean())
# df["Age"] = pd.to_numeric(df["Age"], errors="coerce") #for mean
# df["Age"]=df["Age"].fillna(df["Age"].mean())

print(df["Age"])

print(df)

df1=pd.DataFrame({"Name":["Alicy","BOB"], "Score":[10,None]})

df2=pd.DataFrame({ "Name":["Raj",None], "Score":[90, 10]})

print(df1)
print(df2)


#row wise concatenation
concat_df=pd.concat([df1,df2], axis=0, ignore_index=True)
print(concat_df)


#column wise concatenation
concat_df=pd.concat([df1,df2], axis=1)
print(concat_df)


df1=pd.DataFrame({"ID":[1,2],"Name":["Alicy","BOB"]})

df2=pd.DataFrame({"ID":[2,3], "Score":[90,80] })

print(df1)
print(df2)

result=pd.merge(df1,df2, on="ID", how="outer")
print(result)

result2=pd.merge(left=df1,right=df2, on="ID", how="inner")
print(result2)

result3=pd.merge(left=df1,right=df2, on="ID", how="left")
print(result3)

result4=pd.merge(left=df1,right=df2, on="ID", how="right")
print(result4)


df=pd.read_excel('yelp.xlsx', sheet_name='yelp_data')
print(df.head())

df_cities=pd.read_excel('yelp.xlsx', sheet_name='cities')
print(df_cities)

df_new=pd.merge(left=df, right=df_cities, how="inner", left_on="city_id", right_on="id")
print(df_new)