def dictionary_of_metrics(items):
    """
    Takes a list of items and returns a dictionary of the summary statistics rounded to two decimal places.
    
    Args: 
        items (list): list containing numerical values.
        
    Returns:
         dictionary: containing mean, median, variance, standard deviation, minimum and maximum rounded to two decimal places.
         
    Examples:
         >>> dictionary_of_metrics([1, 8, 3, 2, 7, 4, 9])
             {'mean': 4.86,
             'median': 4.0,
             'var': 9.81,
             'std': 3.13,
             'min': 1,
             'max': 9}
    """
    
    import numpy as np
    n = len(items)
    average = round(np.mean(items), 2)
    median = round(np.median(items), 2)
    variance = round((sum((items-np.mean(items))**2))/(n-1), 2)
    standard_dev = round(((sum((items-np.mean(items))**2))/(n-1))**(1/2), 2)
    minimum = round(min(items), 2)
    maximum = round(max(items), 2)
    
    return {'mean':average,
            'median':median,
            'var':variance,
            'std':standard_dev,
            'min':minimum,
            'max':maximum}
    pass

def five_num_summary(items): 
    """
    Takes a list of items and returns a dictionary of the five number summary rounded to two decimal places.
    
    Args: 
        items (list): list containing numerical values.
        
    Returns:
         dictionary: containing percentiles - maximum, median, minimum, lower quartile and upper quartile rounded to two decimal places.
         
    Examples:
         >>> five_num_summary([1, 8, 3, 2, 7, 4, 9])
             {'max': 9.0,
             'median': 4.0,
             'min': 1.0,
             'q1': 2.5,
             'q3': 7.5}
    """
    
    import numpy as np
    
    percentile = np.percentile(items, [0,25,50,75,100]) #Create a list of desired percentiles
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

    Args:
        dates(list): list with DATETIMEs

    Returns:
        date(list): a list containing a string of DATEs from the DATETIME in the 'yyyy-mm-dd' format 
     """

    #splitting the dates(containing datetime data) list and returning only the datetime
    return([item.split()[0] for item in dates])
    pass
   
def extract_municipality_hashtags(df):
    """
    Extracts the municipalities and hashtags within given tweets

    Args:
        df(dataframe): dataframe with tweets data
    
    Returns(dataframe): dataframe with 2 new columns, 'municipality' and 'hashtag'
                        'municipality' returns the municipality from a tweet using the given dictonary
                        'hashtag' returns the hashtags from a tweet
                        if no municipality or hashtag is found in the tweets, a nan is returned
    """

    import numpy as np
    import pandas as pd
    mun_dict = {'@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'}

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
    pass
  
def number_of_tweets_per_day(df):
    """ 
    Calculates the number of tweets per date
    
    Args:
        df(dataframe): dataframe with twitter data
    
    Returns:
        dataframe: dataframe with columns Date and Tweets.
                   Date column is grouped by Date.
                   Tweets column is total number of tweets per Date
    """
    
    import pandas as pd    

    df['Date'] = pd.to_datetime(df['Date']) #converts date column to datetime
    df['Date'] = df['Date'].dt.date #extract only the date part of the datetime in the date column                         
    twitter_cnt=df.groupby('Date').count() #group the dataframe by unique dates and calculate the number of tweets in each day
    twitter_cnt.reset_index(inplace = True) #reset index
    twitter_cnt.set_index('Date', inplace = True)  #set date column as index 
    
    return twitter_cnt
    pass

def word_splitter(df):
    """
    Takes in pandas DataFrame.DataFrame should contain a column, named 'Tweets'.
    Function Splits the sentences in a dataframe's column 'Tweets' into a list of the separate words
    where all the words are lowercase.
    The list is placed in a new column named 'Split Tweets' in the original dataframe
    
    Args:   
        pandas DataFrame with two columns.
    Returns:
        pandas DataFrame with three columns.
    
    """
    import pandas as pd
 
    df['temp_column']= df['Tweets'].str.lower() #temporary column that contains the tweets in lowercase
    df['Split Tweets']= df['temp_column'].str.rsplit() #splitting the words of temporal column into a new column 'Split tweets'
    df = df.drop('temp_column', 1) #delete temporal column

    return df
    pass

def stop_words_remover(df):
    """ 
    A function that takes a pandas dataframe as an input, tokenises the
    sentences and removes all the stopwords in the input using a stop words
    dictionary and returns a modified version of the pandas dataframe
    
    Args:   
        pandas DataFrame.
    
    Returns:
        pandas DataFrame with removed stopwords.
    """
    stop_words_dict = {'stopwords':['where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon', 
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former', 
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through', 
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to', 
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although', 
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still', 
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose', 
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take', 
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind', 
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next', 
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor', 
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever', 
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least', 
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under', 
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call', 
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all', 
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves', 
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others', 
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody', 
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten', 
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty', 
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine', 
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too', 
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow', 
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our', 
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon', 
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me', 
        'same', 'were', 'it', 'every', 'third', 'together']}
    
    df['Without Stop Words'] = df['Tweets'].apply(str.lower).apply(str.split)

    for i in range(len(df)):
        df['Without Stop Words'][i] = [x for x in df['Without Stop Words'][i] if x not in stop_words_dict['stopwords']]
    return df
    pass
