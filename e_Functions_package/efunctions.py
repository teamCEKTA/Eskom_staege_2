def dictionary_of_metrics(items):
    """Takes a list of items and returns a dictionary of the summary statistics"""
    import numpy
    n = len(items)
    average = round(numpy.mean(items), 2)
    median = round(numpy.median(items), 2)
    variance = round((sum((items-numpy.mean(items))**2))/(n-1), 2)
    standard_dev = round(((sum((items-numpy.mean(items))**2))/(n-1))**(1/2), 2)
    minimum = round(min(items), 2)
    maximum = round(max(items), 2)
    
    return {'mean':average,'median':median,'var':variance,'std':standard_dev,'min':minimum,'max':maximum}
    pass

def five_num_summary(items):
    import numpy as np
    """Takes a list of items and returns a dictionary of the five number summary"""
    
    percentile = np.percentile(items, [0,25,50,75,100]) #A list of percentiles
    minimum = round(percentile[0], 2)
    quartile_1 = round(percentile[1], 2)
    median = round(percentile[2], 2)
    quartile_3 = round(percentile[3], 2)
    maximmu = round(percentile[4], 2)
    
    return {'max':maximmu,'median':median,'min':minimum,'q1':quartile_1,'q3':quartile_3}
    pass

def date_parser(dates):
    """
    Takes a list of datetime strings and converts it into a list of strings
    with only the date
     """

    #splitting the dates(containing datetime data) list and returning only the datetime
    return([item.split()[0] for item in dates])
    pass
   
def extract_municipality_hashtags(df):
    """
    Takes in a pandas dataframe and returns a modified dataframe which 
    extracts the municipality from a tweet using the given dictonary and puts
    them into a new column. It also returns the hashtags from a tweet and
    outputs them into a new column in the same dataframe.The tweets which
    don't have either a municipality or a hashtag, are filled with np.nan.
    The column headers of the new columns are "municipality" & "hashtags"
    respectively.
    """
    import numpy as np
    import pandas as pd
    #creating 'hashtag' and 'municipality' columns with zeros to later replace the zero's
    df['municipality'] = 0
    df['hashtags'] = 0
    
    #Iterating over the columns and rows of the twitter column
    for index,row in df.iterrows():
        splt = row['Tweets'].split()
        for i in splt:
            #extracting all key values that match the keywords in the dictionary, to populate the municipality column
            if i in mun_dict:
                idx = index
                df['municipality'][idx] = mun_dict[i]
        #extracting all hashtags and inserting them as a string in the hashtag column
            if i.startswith("#"): 
                idx = index
                df['hashtags'][idx] = [i.lower() for i in splt if i.startswith("#")]
            
        if df['municipality'][index] == 0:
            df['municipality'][index] = np.nan
        #populating the rest of the columns with nan whereever there isn't a hashtag or municipality keyword
        if df['hashtags'][index] == 0:
            df['hashtags'][index] = np.nan
            
    return df
  
def number_of_tweets_per_day(df):
    """ 
    A function that takes a pandas dataframe as an input and returns a new
    dataframe that is grouped by date, with the number of tweets for each day
    """
    
    df['Date'] = pd.to_datetime(df['Date']) #converts date column to datetime
    df['Date'] = df['Date'].dt.date #extract only the date part of the datetime in the date column                         
    twitter_cnt=df.groupby('Date').count() #group the dataframe by unique dates and calculate the number of tweets in each day
    twitter_cnt.reset_index(inplace = True) #reset index
    twitter_cnt.set_index('Date', inplace = True)  #set date column as index 
    
    return twitter_cnt

def word_splitter(df):
    """
    This function takes in a twitter database.The database originally has 
    two column ,a 'Tweets' and 'Date' column, and returns the database with
    a new "Split Tweets" column. This new column contains the tweets as a list
    of separate words and all words are lowercase
    """
 
    df['temp_column']= df['Tweets'].str.lower() #temporary column that contains the tweets in lowercase
    df['Split Tweets']= df['temp_column'].str.rsplit() #splitting the words of temporal column into a new column 'Split tweets'
    df = df.drop('temp_column', 1) #delete temporal column

    return df

def stop_words_remover(df):
    """ 
    A function that takes a pandas dataframe as an input, tokenises the
    sentences and removes all the stopwords in the input using a stop words
    dictionary and returns a modified version of the pandas dataframe
    """
    
    df['Without Stop Words'] = df['Tweets'].apply(str.lower).apply(str.split)

    for i in range(len(twitter_df)):
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if x not in stop_words_dict['stopwords']]
    return df
    pass
