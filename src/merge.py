import pandas as pd 

def makedf(file1: str, file2: str) -> pd.DataFrame:
    df1 = pd.read_csv(file1,delimiter=',', encoding='utf-8')
    df2 = pd.read_csv(file2,delimiter=';', encoding='utf-8')
    
    df1['energy'] = df1['energy'].astype(str)
    df1['energy'] = df1['energy'].str.replace('.', ',', regex=False)
    
    merge_df = pd.merge(df1,df2,left_on='date',right_on='DataHora', how='left')
    
    merge_df.drop(columns=['DataHora','data_atualizacao'], inplace=True)
    return merge_df 

if __name__ == "__main__":
    result = makedf('/media/lucas/Files/2.Projetos/0.mylake/gold/solar_project/all_data.csv', '/media/lucas/Files/2.Projetos/0.mylake/silver/clima/all_data.csv')
    result.to_csv('/media/lucas/Files/2.Projetos/0.mylake/gold/clima/clima_solar_all_datas.csv',index=False ,sep=';', encoding='utf-8')
        
        
# df1 = pd.read_csv('/media/lucas/Files/2.Projetos/0.mylake/gold/solar_project/all_data.csv',delimiter=',', encoding='utf-8')
# print(df1)
    