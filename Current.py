import pandas as pd
import numpy as np

info_sc = pd.read_csv(r'C:\Users\Crist\Python\Data\Data_scuole_roma.csv',index_col=['plesso_id_meccanografico']).drop_duplicates()
scuole = pd.read_csv(r'C:\Users\Crist\Python\Data\Scuole_domanda.csv',index_col='id_meccanografico')
elementari = pd.read_csv(r'C:\Users\Crist\Python\Data\temp.csv')
print(info_sc)
print(scuole)
print(elementari)
#print(pd.concat([info_sc, scuole], axis=1, join="inner"))


print(scuole.index.duplicated().any())
print(info_sc.index.duplicated().any())


#print(pd.merge(info_sc, scuole, on='id_meccanografico'))

#print(info_sc.index.get_level_values(0).values)

for row in scuole.index.values:
    if(row[0] in info_sc.index.get_level_values(0).values):
        print(row)
        
print('RMEE00700R' in info_sc.index.get_level_values(0).values)
print('RMEE00700R' in info_sc['istituto_principale_id_meccanografico'].values)

df = elementari[elementari['Unnamed: 1'].notna()]
print(df.head(10))

test_data = ['RMEE00701T','RMEE17201T','RMEE20501X','RMEE220012','RMEE22101T','RMEE27801N','RMEE30701C','RMEE309014','RMEE80101T','RMEE804019','RMEE805015']


for row in test_data:
    if(row in info_sc.index.get_level_values(0).values):
        print(row)