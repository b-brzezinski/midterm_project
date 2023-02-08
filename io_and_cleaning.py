import pandas as pd

class EmptyTimeframe(Exception):
    pass

def input_data(gdp_file,pop_file,fos_file):
    """
    this function takes a tuple of paths to csv files concerning gdp, population and CO2 emissions and returns a tuple of dataframes taken from those csv files.
    """
    gdp_data=pd.read_csv(gdp_file,header=2)
    pop_data=pd.read_csv(pop_file,header=2)
    fos_data=pd.read_csv(fos_file,header=0)
    return gdp_data,pop_data,fos_data
def clean_fos_data(fos_data):
    fos_data = fos_data.replace('VIET NAM','VIETNAM', )
    fos_data = fos_data.replace('CHINA (MAINLAND)','CHINA')
    fos_data = fos_data.replace('CZECH REPUBLIC','CZECHIA')
    fos_data = fos_data.replace('FEDERATED STATES OF MICRONESIA','MICRONESIA, FED. STS.')
    fos_data = fos_data.replace('UNITED STATES OF AMERICA','UNITED STATES')
    fos_data = fos_data.replace('BOSNIA & HERZEGOVINA','BOSNIA AND HERZEGOVINA')
    fos_data = fos_data.replace('ISLAMIC REPUBLIC OF IRAN','IRAN, ISLAMIC REP.')
    fos_data = fos_data.replace('SAINT LUCIA','ST. LUCIA')
    fos_data = fos_data.replace('VENEZUELA','VENEZUELA, RB')
    fos_data = fos_data.replace('TURKEY','TURKIYE')
    fos_data = fos_data.replace('SAMOA','AMERICAN SAMOA')
    fos_data = fos_data.replace('COTE D IVOIRE','COTE D\'IVOIRE')
    fos_data = fos_data.replace('MACEDONIA','NORTH MACEDONIA')
    fos_data = fos_data.replace('KYRGYZSTAN','KYRGYZ REPUBLIC')
    fos_data = fos_data.replace('YEMEN','YEMEN REP.')
    fos_data = fos_data.replace('LIBYAN ARAB JAMAHIRIYAH','LIBYA')
    fos_data = fos_data.replace('UNITED REPUBLIC OF TANZANIA','TANZANIA')
    fos_data = fos_data.replace('ST. KITTS-NEVIS-ANGUILLA','ST. KITTS AND NEVIS')
    fos_data = fos_data.replace('ST. KITTS-NEVIS','ST. KITTS AND NEVIS')
    fos_data = fos_data.replace('CAPE VERDE','CABO VERDE')
    fos_data = fos_data.replace('GAMBIA','GAMBIA, THE')
    fos_data = fos_data.replace('DEMOCRATIC REPUBLIC OF THE CONGO (FORMERLY ZAIRE)','CONGO, DEM. REP.')
    fos_data = fos_data.replace('HONG KONG SPECIAL ADMINSTRATIVE REGION OF CHINA','HONG KONG SAR, CHINA')
    fos_data = fos_data.replace('EAST & WEST PAKISTAN','PAKISTAN')
    fos_data = fos_data.replace('SLOVAKIA','SLOVAK REPUBLIC')
    fos_data = fos_data.replace('DEMOCRATIC PEOPLE S REPUBLIC OF KOREA','KOREA, DEM. PEOPLE\'S REP.')
    fos_data = fos_data.replace('TIMOR-LESTE (FORMERLY EAST TIMOR)','TIMOR-LESTE')
    fos_data = fos_data.replace('PLURINATIONAL STATE OF BOLIVIA','BOLIVIA')
    fos_data = fos_data.replace('FRANCE (INCLUDING MONACO)','FRANCE')
    fos_data = fos_data.replace('EGYPT','EGYPT, ARAB REP.')
    fos_data = fos_data.replace('CONGO','CONGO, REP.')
    fos_data = fos_data.replace('MYANMAR (FORMERLY BURMA)','MYANMAR')
    fos_data = fos_data.replace('FEDERAL REPUBLIC OF GERMANY','GERMANY')
    fos_data = fos_data.replace('ANTIGUA & BARBUDA','ANTIGUA AND BARBUDA')
    fos_data = fos_data.replace('REPUBLIC OF SOUTH SUDAN','SOUTH SUDAN')
    fos_data = fos_data.replace('BAHAMAS','BAHAMAS, THE')
    fos_data = fos_data.replace('SAO TOME & PRINCIPE','SAO TOME AND PRINCIPE')
    fos_data = fos_data.replace('GUINEA BISSAU','GUINEA-BISSAU')
    fos_data = fos_data.replace('LAO PEOPLE S DEMOCRATIC REPUBLIC','LAO PDR')
    fos_data = fos_data.replace('REPUBLIC OF MOLDOVA','MOLDOVA')
    fos_data = fos_data.replace('SAINT MARTIN (DUTCH PORTION)','SINT MAARTEN (DUTCH PART)')
    fos_data = fos_data.replace('REPUBLIC OF CAMEROON','CAMEROON')
    fos_data = fos_data.replace('ITALY (INCLUDING SAN MARINO)','ITALY')
    fos_data = fos_data.replace('REPUBLIC OF SUDAN','SUDAN')
    fos_data = fos_data.replace('REPUBLIC OF KOREA','KOREA, REP.')
    fos_data = fos_data.replace('BRUNEI (DARUSSALAM)','BRUNEI DARUSSALAM')
    fos_data = fos_data.replace('FAEROE ISLANDS','FAROE ISLANDS')
    fos_data = fos_data.replace('MACAU SPECIAL ADMINSTRATIVE REGION OF CHINA','MACAO SAR, CHINA')
    fos_data = fos_data.replace('ST. VINCENT & THE GRENADINES','ST. VINCENT AND THE GRENADINES')
    fos_data = fos_data.replace('JAPAN (EXCLUDING THE RUYUKU ISLANDS)','JAPAN')
    fos_data = fos_data.replace('RWANDA-URUNDI','RWANDA')
    fos_data = fos_data.drop(fos_data[fos_data['Country'].isin(['ANTARCTIC FISHERIES','REUNION','KUWAITI OIL FIRES'])].index)
    return fos_data

def clean_gdp_pop_data(data):
    data = data.drop(data[data['Country Name'].isin(['Africa Eastern and Southern',
                  'Africa Western and Central',
                  'Central Europe and the Baltics',
                  'Early-demographic dividend',
                  'East Asia & Pacific',
                  'East Asia & Pacific (excluding high income)',
                  'East Asia & Pacific (IDA & IBRD countries)',
                  'Europe & Central Asia',
                  'Europe & Central Asia (excluding high income)',
                  'Europe & Central Asia (IDA & IBRD countries)',
                  'European Union',
                  'Fragile and conflict affected situations',
                  'Heavily indebted poor countries (HIPC)',
                  'IDA & IBRD total',
                  'IDA only',
                  'IDA blend',
                  'Latin America & the Caribbean (IDA & IBRD countries)',
                  'Latin America & Caribbean (excluding high income)',
                  'Latin America & Caribbean',
                  'Late-demographic dividend',
                  'Lower middle income',
                  'Low income',
                  'Low & middle income',
                  'Middle income',
                  'Middle East & North Africa (IDA & IBRD countries)',
                  'Middle East & North Africa (excluding high income)',
                  'Middle East & North Africa',
                  'OECD members',
                  'Pre-demographic dividend',
                  'South Asia (IDA & IBRD)',
                  'South Asia',
                  'Sub-Saharan Africa (IDA & IBRD countries)',
                  'Sub-Saharan Africa (excluding high income)',
                  'Sub-Saharan Africa',
                  'Arab World',
                  'Least developed countries: UN classification',
                  'Upper middle income',
                  'World',
                  'Small States',
                  'High income',
                  'North America',
                  'IDA total',
                  'Post-demographic dividend',
                  'Other small states',
                  'IBRD only',
                  'Euro area'
                  ])].index)
    return data
def _timeframe(gdp_data,pop_data,fos_data):
    """
    An internal function that returns all the valid years for given tuple of dataframes.
    """
    set_gdp=set(gdp_data.columns)
    set_pop=set(pop_data.columns)
    set_fos=set(str(i) for i in fos_data['Year'])
    return list(set.intersection(set_gdp,set_pop,set_fos))

def join_dataframes(gdp_data,pop_data,fos_data):
    """
    This function modifies gdp_data and pop_data into melted dataframes, so they are able to be joined with fos_data and used in further analysis.
    It also prints the list of countries that were ommited in the returned dataframe.
    """
    time_interval=_timeframe(gdp_data,pop_data,fos_data)
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
    gdp_countries = set(gdp_melt['Country Name'])
    pop_countries = set(pop_melt['Country Name'])
    fos_countries = set(fos_data['Country Name'])
    countries_union = gdp_countries | pop_countries | fos_countries
    countries_inter = set(joined_df['Country Name'])
    if len(countries_union - countries_inter)>0:
        print(f'countries that are not present in joined dataframe: {countries_union - countries_inter}')
    return joined_df

def filtering_data(data,start=None,finish=None):
    """
    this function is filtering data based on given parameters start and finish.
    If the given timeframe ends up empty, the function will print the error and proceed with returning the whole dataframe.
    """
    try:
        if (start is None) & (finish is None):
            filtered = data.copy()
        elif start is None:
            filtered = data[data['Year']<=int(finish)].copy()
        elif finish is None:
            filtered = data[data['Year']>=int(start)].copy()
        else:
            filtered = data[(data['Year']>=int(start)) & (data['Year']<=int(finish))].copy()
        if filtered.empty:
            raise EmptyTimeframe('Given timeframe is empty.')
        else:
            return filtered
    except EmptyTimeframe:
        print('given timeframe is empty, working on whole data instead.')
        return data
