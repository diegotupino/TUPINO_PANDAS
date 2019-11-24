import pandas as pd
df = pd.read_csv('cars.csv')
print(df.iloc[0:5,0::2])

print(df.loc[0,'Model':])

print(df.loc[[23],['Model']])

print(df.loc[[1,18,28],['Model','cyl','gear']])
