from mypackage import myModule

def dictionary_of_metrics():
    
    assert dictionary_of_metrics(gauteng) == {'mean': 26244.42,
                                   'median': 24403.5,
                                   'var': 108160153.17,
                                   'std': 10400.01,
                                   'min': 8842.0,
                                   'max': 39660.0}, 'incorrect'

def five_num_summary():

    assert five_num_summary(gauteng) == {
        'max': 39660.0,
        'median': 24403.5,
        'min': 8842.0,
        'q1': 18653.0,
        'q3': 36372.0
    }, 'incorrect'

def date_parser():
    
    assert date_parser(dates[:3]) == ['2019-11-29', '2019-11-29', '2019-11-29'], 'incorrect'
    assert date_parser(dates[-3:]) == ['2019-11-20', '2019-11-20', '2019-11-20'], 'incorrect'

def stop_words_remover(df):
    assert stop_words_remover(twitter_df.copy()).loc[0, "Without Stop Words"] == ['@bongadlulane', 'send', 'email', 'mediadesk@eskom.co.za']
    assert stop_words_remover(twitter_df.copy()).loc[100, "Without Stop Words"] == ['#eskomnorthwest', '#mediastatement', ':', 'notice', 'supply', 'interruption', 'lichtenburg', 'area', 'https://t.co/7hfwvxllit']