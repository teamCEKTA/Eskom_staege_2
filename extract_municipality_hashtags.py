def extract_municipality_hashtags(df):
    df['hashtags'] = 0
    df['municipality'] = 0

    for index,row in df.iterrows():
        splt = row['Tweets'].split()
        for i in splt:
            if i.startswith("#"):
                idx = index
                df['hashtags'][idx] = [i for i in splt if i.startswith("#")]
            if i in mun_dict:
                idx = index
                df['municipality'][idx] = mun_dict[i]
        if df['hashtags'][index] == 0:
            df['hashtags'][index] = np.nan
            
        if df['municipality'][index] == 0:
            df['municipality'][index] = np.nan
    return df