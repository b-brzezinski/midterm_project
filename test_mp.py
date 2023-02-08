#this test is used by opening the script in interactive mode and manualy checking dataframes whether they make sense

import io_and_cleaning
import analysis
import pandas as pd

gdp_file = 'data/GDP/API_NY.GDP.MKTP.CD_DS2_en_csv_v2_4751562.csv'
pop_file = 'data\population\API_SP.POP.TOTL_DS2_en_csv_v2_4751604.csv'
fos_file = 'data\Fossil\data\\fossil-fuel-co2-emissions-by-nation_csv.csv'

gdp_data,pop_data,fos_data = io_and_cleaning.input_data(gdp_file,pop_file,fos_file)
data_joined=io_and_cleaning.join_dataframes(gdp_data,pop_data,fos_data)

#filtering
data_nfiltered=io_and_cleaning.filtering_data(data_joined)
data_filtered_90s=io_and_cleaning.filtering_data(data_joined,1990,2000)
data_filtered_empty=io_and_cleaning.filtering_data(data_joined,2001,2000)
data_filtered_1k=io_and_cleaning.filtering_data(data_joined,finish=2001)
data_filtered_2k=io_and_cleaning.filtering_data(data_joined,start=2001)
data_filtered_5y=io_and_cleaning.filtering_data(data_joined,2001,2000)
#analysis
analysis.biggest_emmiters(data_filtered_2k)
analysis.biggest_gdp(data_filtered_2k)
analysis.co2_change(data_filtered_2k)
analysis.co2_change(data_filtered_5y)