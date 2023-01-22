import pandas as pd
import numpy as np

def input(gdp_file,pop_file,fos_file):
    gdp_data=pd.read_csv(gdp_file,header=1)
    pop_data=pd.read_csv(pop_file,header=1)
    fos_data=pd.read_csv(fos_file,header=0)
    return gdp_data,pop_data,fos_data

def filtering_data(data,start='nan',finish='nan'):
    if type(start) == str and type(finish) == str:
        return data
    elif type(start) == str:
        filtered = data[data['Year']<=finish]
    elif type(finish) == str:
        filtered = data[data['Year']==start]
    else:
        filtered = data[(data['Year']>=start) & (data['Year']<=finish)]
    return filtered


if __name__ == "__main__":
    gdp_data,pop_data,fos_data=input('data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv','data\population\API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv','data\Fossil\data\\fossil-fuel-co2-emissions-by-nation_csv.csv')
    data_filtered=filtering_data(fos_data,1990,2000)
    
