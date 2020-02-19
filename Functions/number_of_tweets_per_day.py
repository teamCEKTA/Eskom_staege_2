def number_of_tweets_per_day(df):
  ### Code Here
    #df = df['Date'].to_list()
    df['Date'] = pd.to_datetime(df['Date'])
    df['Date'] =  df['Date'].dt.date                            
    #twitter_df['Date'] = pd.DataFrame([item.split()[0] for item in dates],columns=["Date"])   
    twitter_cnt=twitter_df.groupby('Date').count()
    twitter_cnt.reset_index(inplace=True)
    twitter_cnt.set_index('Date', inplace=True)   
    
    return twitter_cnt

number_of_tweets_per_day(twitter_df)