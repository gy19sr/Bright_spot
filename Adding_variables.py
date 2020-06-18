pip.install(pymc3)

import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('inverts_database_CSV.csv', encoding = "ISO-8859-1", engine='python')

df = df.drop(['Date','management', 'Ecoregion', 'den_per_HA', 'density_for_summed_transect area_#permeter'], axis=1)
df = df.drop(['den_for_transect_#permeter', 'total transect area', 'Transect_area', 't_Width', 't_Length', 'Abundance', 'habitat_type', 'total number of transect'], axis= 1)
df['den'] = df['den_per_100m2']
df['den'] = pd.to_numeric(df['den'], errors='coerce') # make den a float

print(df.head())
#df.to_csv(r'C:/Users/stuar/Documents/GitHub/Bright_spot/Inverts_DB/DB_edited.csv', index=False) # saving as csv

df.info() #to see the columns type

# print(df.den.value_counts())
# print("den is null", df[df.den.isnull()]) # there are no nulls in den



# print(df[(df['den'] >= 0.10)])
"""
# practice looping
# so i means each row value in df.den
for i in df.den:
    if i == .25:
        print('found!')
        break
    else:
        print('failed')

"""
#print(df['country'].value_counts())
# practice with quick data grabbing
#testdf = df[((df.country == 'Philippines') & (df.den >= .81))]
#print(testdf.head())
#print(testdf['country'].value_counts())


# discover year distribution

df = df.dropna(axis=0, subset=['Year'],inplace=False)
print(df['Year'].value_counts())

histo = df['Year']
print(sns.distplot( ))

