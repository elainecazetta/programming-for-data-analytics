# Preparing the cso-population by age file for analysis
# Author: Andrew Beatty
# Reproduced by: Elaine Cazetta

import pandas as pd

FILENAME = "cso-populationbyage.csv"
DATADIR = "../Topic 5/"
FULLPATH = DATADIR + FILENAME

df = pd.read_csv(FULLPATH)

drop_col_list = ["STATISTIC","Statistic Label","TLIST(A1)","CensusYear","C02199V02655",
                 "Sex","C02076V03371","C03789V04537","UNIT"]

df.drop(columns=drop_col_list, inplace=True)

df = df[df["Single Year of Age"] != "All ages"]
df["Single Year of Age"] = df["Single Year of Age"].str.replace('Under 1 year', '0')
df["Single Year of Age"] = df["Single Year of Age"].str.replace('\D', '', regex=True)

df["Single Year of Age"] = df["Single Year of Age"].astype('int64')

df_anal = pd.pivot_table(df, 'VALUE','Single Year of Age','Administrative Counties')

print(df_anal.head(10))
df_anal.to_csv("population_for_analysis_.csv")
