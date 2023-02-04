import pandas as pd
import numpy as np

class EmptyTimeframe(Exception):
    pass

def input(gdp_file,pop_file,fos_file):
    gdp_data=pd.read_csv(gdp_file,header=2)
    pop_data=pd.read_csv(pop_file,header=2)
    fos_data=pd.read_csv(fos_file,header=0)
    return gdp_data,pop_data,fos_data

def timeframe(gdp_data,pop_data,fos_data):
    set_gdp=set(gdp_data.columns)
    set_pop=set(pop_data.columns)
    set_fos=set(str(i) for i in fos_data['Year'])
    return list(set.intersection(set_gdp,set_pop,set_fos))

def join_dataframes(gdp_data,pop_data,fos_data):
    time_interval=timeframe(gdp_data,pop_data,fos_data)
    gdp_melt=gdp_data.melt(id_vars="Country Name",value_vars=time_interval,var_name='Year',value_name='GDP')
    gdp_melt['Year']=gdp_melt['Year'].apply(int)
    gdp_melt.dropna(subset=['GDP'], inplace=True)
    gdp_melt['Country Name']=gdp_melt['Country Name'].str.upper()
    pop_melt=pop_data.melt(id_vars="Country Name",value_vars=time_interval,var_name='Year',value_name='Population')
    pop_melt['Year']=pop_melt['Year'].apply(int)
    pop_melt.dropna(subset=['Population'], inplace=True)
    pop_melt['Country Name']=pop_melt['Country Name'].str.upper()
    fos_data.rename(columns={'Country':'Country Name','Total':'Total CO2'}, inplace=True)
    joined_df = pd.merge(gdp_melt, pop_melt,how='inner', left_on=['Country Name','Year'], right_on=['Country Name','Year'])
    joined_df = pd.merge(joined_df, fos_data[['Country Name','Year','Total CO2']], how='inner', left_on=['Country Name','Year'], right_on=['Country Name','Year'])
    return joined_df

def filtering_data(data,start='nan',finish='nan'):
    try:
        if type(start) == str and type(finish) == str:
            return data
        elif type(start) == str:
            filtered = data[data['Year']<=finish]
        elif type(finish) == str:
            filtered = data[data['Year']>=start]
        else:
            filtered = data[(data['Year']>=start) & (data['Year']<=finish)]
        if filtered.empty:
            raise EmptyTimeframe('Given timeframe is empty.')
        else:
            return filtered
    except EmptyTimeframe:
        print('given timeframe is empty, working on whole data instead.')
        return data

if __name__ == "__main__":
    gdp_data,pop_data,fos_data=input('data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv','data\population\API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv','data\Fossil\data\\fossil-fuel-co2-emissions-by-nation_csv.csv')
    data_joined=join_dataframes(gdp_data,pop_data,fos_data)
    data_filtered=filtering_data(data_joined,1990,2000)
    data_filtered.to_csv('test.csv')
    
    
