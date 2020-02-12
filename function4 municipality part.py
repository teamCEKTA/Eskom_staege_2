import pandas as pd
import numpy as np

url = 'https://raw.githubusercontent.com/RidhaMoosa/eskom_data-/master/twitter_nov_2019.csv'
twitter_df = pd.read_csv(url)
twitter_df.head()

municipality_dict = { '@CityofCTAlerts' : 'Cape Town',
            '@CityPowerJhb' : 'Johannesburg',
            '@eThekwiniM' : 'eThekwini' ,
            '@EMMInfo' : 'Ekurhuleni',
            '@centlecutility' : 'Mangaung',
            '@NMBmunicipality' : 'Nelson Mandela Bay',
            '@CityTshwane' : 'Tshwane'}

def extract_municipality(df):

    twitter_df['municipality'] = 0
    for index,row in twitter_df.iterrows():
        spl = row['Tweets'].split()
        for i in spl:
            if i in municipality_dict:
                idx = index
                twitter_df['municipality'][idx] = municipality_dict[i]

        if twitter_df['municipality'][index] == 0:
            twitter_df['municipality'][index] = np.nan

    return twitter_df

    extract_municipality(twitter_df).iloc[:11, :10]