import pandas as pd

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

def co2_change(data):
    timeframe=min(10,max(data['Year'])-min(data['Year']))
    sta_data=data[data['Year']==(max(data['Year'])-timeframe)].rename(columns={'Total CO2':f'CO2 in {max(data.Year)-timeframe}'})
    end_data=data[data['Year']==max(data['Year'])].rename(columns={'Total CO2':f'CO2 in {max(data.Year)}'})
    new_data=pd.merge(sta_data[['Country Name',f'CO2 in {max(data.Year)-timeframe}']],end_data[['Country Name',f'CO2 in {max(data.Year)}']], how='inner', on='Country Name')
    new_data['Change in CO2']=new_data[f'CO2 in {max(data.Year)}']/new_data[f'CO2 in {max(data.Year)-timeframe}']
    return new_data.sort_values(by='Change in CO2').head(15)

if __name__ == '__main__':
    df=pd.read_csv('test.csv',header=0,index_col=0)
    df_mod1=biggest_emmiters(df)
    df_mod2=biggest_gdp(df)
    df_mod3=co2_change(df)
    