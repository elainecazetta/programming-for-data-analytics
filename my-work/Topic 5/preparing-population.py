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

print(df.head(3))