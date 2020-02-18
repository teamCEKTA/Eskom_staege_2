Metric Dictionary

The metric dictionary function calculates the mean, median, variance, standard deviation, minimum and maximum of a list of items and  returns them in the form of a dictionary.


Five Number Summary Dictionary

The five number summary function takes a list of items and calculates the minimum, lower quartile, median, upper quartile and maximum and returns them in the form of a dictionary.


Date Parser

The function  takes a list of strings as input.
Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'.
The function returns a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.


Hashtag & Municipality Remover

takes a pandas dataframe as input.
Extract the municipality from a tweet using the given dictionary called ‘ mun_dict’, and insert the result into a new column named 'municipality' in the same dataframe.
Use the entry np.nan when a municipality is not found.
Extract a list of hashtags from a tweet into a new column named 'hashtags' in the same dataframe.
Use the entry np.nan when no hashtags are found.


Number of Tweets per Day

takes a pandas dataframe as input.
It  returns a new dataframe, grouped by day, with the number of tweets for that day.
The index of the new dataframe is named Date, and the column of the new dataframe is 'Tweets', corresponding to the date and number of tweets, respectively.
The date is formated as yyyy-mm-dd, and is a datetime object.


Word Splitter

takes a pandas dataframe as an input.
the dataframe  contains a column, named 'Tweets'.
split the sentences in the 'Tweets' into a list of seperate words, and place the result into a new column named 'Split Tweets'. 
The resulting words are all  lowercase!
modify the input dataframe directly.
returns the modified dataframe.


Stopwords & Link Remover

This function takes a pandas dataframe as input and removes all the stopwords in the input and returns a modified version of the pandas dataframe.
