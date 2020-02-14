#Function 7
def stop_words_http_remover(df):
    df['Without Stop Words'] = df['Tweets'].apply(str.lower).apply(str.split)

    for i in range(len(twitter_df)):
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if x not in stop_words_dict['stopwords']]
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if "http" not in x]
    pass
