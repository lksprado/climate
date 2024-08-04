import os
import glob
import pandas as pd
from  datetime import datetime 

def concatenate(input_folder: str) -> pd.DataFrame:
    dfs = []

    for csv in glob.glob(os.path.join(input_folder, '*.csv')):
        df = pd.read_csv(csv,delimiter=';', encoding='utf-8')
        dfs.append(df)
    
    final_df = pd.concat(dfs, ignore_index=True)

    return final_df

    

def transform(df: pd.DataFrame) -> pd.DataFrame:
    
    df['Hora (UTC)'] = df['Hora (UTC)'].apply(lambda x: f"{x // 100:02}:00")
    df['DataHora'] = df['Data'] + ' '+ df['Hora (UTC)'].astype(str)
    df['DataHora'] = pd.to_datetime(df['DataHora'], format='%d/%m/%Y %H:%M')
    df['DataHora'] = df['DataHora']-pd.Timedelta(hours=3)
    df.drop(columns=['Data','Hora (UTC)'], inplace=True)
    first_column = df.pop('DataHora') 
    df.insert(0, 'DataHora', first_column) 
    
    return df

if __name__ == "__main__":
    data = concatenate('/media/lucas/Files/2.Projetos/clima/data/')
    data_new = transform(data)
    data_new.to_csv('/media/lucas/Files/2.Projetos/0.mylake/silver/clima/all_data.csv',index=False ,sep=';', encoding='utf-8')
