import pandas as pd
d=pd.read_excel("F:\\INPUT1.xlsx")
df=pd.DataFrame(d)

filt = (df["VCHTYPE"] == 'Receipt') & (df["VOUCHERTYPENAME"] == 'Receipt')
filtered_df = df.loc[filt, ["DATE","AMOUNT","ALTERID","MASTERID","VCHTYPE","VOUCHERTYPENAME"]]
print(filtered_df)

