import pandas as pd
from numba import jit

def biggest_emmiters(data):
    data['CO2pc']=data['Total CO2']/data['Population']
    grouped = data.groupby('Year')
    df=pd.DataFrame()
    for key, group in grouped:
        sorted= group.sort_values(by='CO2pc',ascending=False,ignore_index=True).head(5)
        df=pd.concat([df,sorted])
    df.index.name='position'
    df.reset_index(inplace=True)
    df['position']+=1
    df=df[['Year','position','Country Name','CO2pc','Total CO2']]
    df_pivot=pd.pivot_table(df,index=['Year','position','Country Name'])
    return df_pivot
def biggest_gdp(data):
    data['GDPpc']=data['GDP']/data['Population']
    grouped = data.groupby('Year')
    df=pd.DataFrame()
    for key, group in grouped:
        sorted= group.sort_values(by='GDPpc',ascending=False,ignore_index=True).head(5)
        df=pd.concat([df,sorted])
    df.index.name='position'
    df.reset_index(inplace=True)
    df['position']+=1
    df=df[['Year','position','Country Name','GDPpc','GDP']]
    df_pivot=pd.pivot_table(df,index=['Year','position','Country Name'])
    return df_pivot
def biggest_gdp(data):
    data['GDPpc']=data['GDP']/data['Population']
    grouped = data.groupby('Year')
    df=pd.DataFrame()
    for key, group in grouped:
        sorted= group.sort_values(by='GDPpc',ascending=False,ignore_index=True).head(5)
        df=pd.concat([df,sorted])
    df.index.name='position'
    df.reset_index(inplace=True)
    df['position']+=1
    df=df[['Year','position','Country Name','GDPpc','GDP']]
    df_pivot=pd.pivot_table(df,index=['Year','position','Country Name'])
    return df_pivot
if __name__ == '__main__':
    df=pd.read_csv('test.csv',header=0,index_col=0)
    df_mod=biggest_emmiters(df)