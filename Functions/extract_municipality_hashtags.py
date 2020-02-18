def extract_municipality_hashtags(df):
    """takes in a pandas dataframe and returns the same dataframe which is modified to extract the municipality from a tweet using the given dictonary into a new column in the same dataframe and hashtag from a tweet into a new column in the same data frame 
with the column headers being "municipality" & "hashtags" respectively and for those tweets which don't have the either a municipality nor a hashtag, np.nan is filled."""
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
