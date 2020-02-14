#Function 7

def stop_words_http_remover(df):
    """ A function that takes a pandas dataframe as an input, tokenises the
    sentences and removes all the stopwords in the input using a stop words
    dictionary and returns a modified version of the pandas dataframe
    """
    df['Without Stop Words'] = df['Tweets'].apply(str.lower).apply(str.split)

    for i in range(len(twitter_df)):
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if x not in stop_words_dict['stopwords']]
    return df
    pass
    
