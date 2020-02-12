def number_of_tweets_per_day(df):
  ### Code Here
    #df = df['Date'].to_list()
    b = pd.DataFrame([item.split()[0] for item in df],columns=["Date"])

    date = pd.DataFrame(b['Date'].value_counts(),columns=["Date","Tweets"])

    date.reset_index(inplace=True)

    date.drop(['Tweets'],axis=1,inplace=True)

    date.columns = ['Date', 'Tweets']
    
    #date.sort_values('Date')
    
    return date