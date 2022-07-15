import pandas as pd

df1 = pd.DataFrame({
    'A':[],
    'B':[]
})

df2 = pd.DataFrame({
    'A': [1,1,3,4,5],
    'B': [1,2,3,4,5]
})

df_concat = pd.concat([df1, df2], axis=0)

print(df_concat)
