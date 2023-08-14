import pandas

df = pandas.read_csv("files/TG_STAID000001.txt", skiprows=20, parse_dates=["    DATE"])
# print(df[10:30])
# print(df.columns)
# print(df["   TG"])
# Simple statistics and filtering

print(df.loc[df["   TG"] != -9999]["   TG"].max() / 10)
print(df.loc[df["   TG"] != -9999]["   TG"].min() / 10)
print(df.loc[df["   TG"] != -9999]["   TG"].mean() / 10)
print(df["   TG"].hist())
