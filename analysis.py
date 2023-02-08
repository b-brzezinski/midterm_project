import pandas as pd

def biggest_emmiters(data):
    """
    this function takes an aggregated dataframe and returns 5 biggest emmiters per capita in each given year.
    """
    data_copy=data.copy()
    data_copy['CO2pc']=data_copy['Total CO2']/data_copy['Population']
    data_copy['CO2pc']=data_copy['CO2pc'].round(decimals= 6)
    grouped = data_copy.groupby('Year')
    new_df=pd.DataFrame()
    for key, group in grouped:
        sorted_group= group.sort_values(by='CO2pc',ascending=False,ignore_index=True).head(5)
        new_df=pd.concat([new_df,sorted_group])
    new_df.index.name='position'
    new_df.reset_index(inplace=True)
    new_df['position']+=1
    new_df=new_df[['Year','position','Country Name','CO2pc','Total CO2']]
    df_pivot=pd.pivot_table(new_df,index=['Year','position','Country Name'])
    return df_pivot


def biggest_gdp(data):
    """
    This function takes an aggregated dataframe and returns 5 countries with highest gpd in each given year.
    """
    data_copy=data.copy()
    data_copy['GDPpc']=data_copy['GDP']/data_copy['Population']
    data_copy['GDPpc']=data_copy['GDPpc'].round(decimals= 2)
    grouped = data_copy.groupby('Year')
    new_df=pd.DataFrame()
    for key, group in grouped:
        sorted_group= group.sort_values(by='GDPpc',ascending=False,ignore_index=True).head(5)
        new_df=pd.concat([new_df,sorted_group])
    new_df.index.name='position'
    new_df.reset_index(inplace=True)
    new_df['position']+=1
    new_df=new_df[['Year','position','Country Name','GDPpc','GDP']]
    df_pivot=pd.pivot_table(new_df,index=['Year','position','Country Name'])
    return df_pivot

def co2_change(data):
    """
    This function takes the dataframe and compares latest year's co2 emissions with 10 years back (or oldest available data) and gives a dataframe of 15 (roughly 10%) best performers.
    """
    timeframe=min(10,max(data['Year'])-min(data['Year']))
    sta_data=data[data['Year']==(max(data['Year'])-timeframe)].rename(columns={'Total CO2':f'CO2 in {max(data.Year)-timeframe}'}).copy()
    end_data=data[data['Year']==max(data['Year'])].rename(columns={'Total CO2':f'CO2 in {max(data.Year)}'}).copy()
    new_data=pd.merge(sta_data[['Country Name',f'CO2 in {max(data.Year)-timeframe}']],end_data[['Country Name',f'CO2 in {max(data.Year)}']], how='inner', on='Country Name')
    new_data['Change in CO2']=new_data[f'CO2 in {max(data.Year)}']/new_data[f'CO2 in {max(data.Year)-timeframe}']
    new_data['Change in CO2']=new_data['Change in CO2'].round(decimals= 3)
    return new_data.sort_values(by='Change in CO2').head(15)

if __name__ == '__main__':
    df=pd.read_csv('test.csv',header=0,index_col=0)
    df_mod1=biggest_emmiters(df)
    df_mod2=biggest_gdp(df)
    df_mod3=co2_change(df)
    