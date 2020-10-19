import pandas as pd

def data_type(data):
    return dataframe[data]


def data_parser(DF):
    DF.rename(columns={'day/month': 'Date'}, inplace=True)
    DF['Time'] = pd.to_datetime(DF['Time']).dt.strftime('%H:%M')
    DF['Wind Speed'] = DF['Wind Speed'].replace('\D', '', regex=True).astype(int)
    DF['Wind Gust'] = DF['Wind Gust'].replace(r'[a-z]', '', regex=True).astype(int)
    DF['Pressure'] = DF['Pressure'].replace(',', '.', regex=True).astype(float)
    DF['Date'] = DF['Date'] + '.2019'
    DF['Humidity'] = DF['Humidity'].str.rstrip('%').astype('float')

    return DF


DATAFRAME = pd.read_csv('DATABASE.csv', sep=';')
dataframe = data_parser(DATAFRAME)
#print(dataframe)
