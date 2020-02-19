FUNCTIONS TO CALCULATE METRICS FROM ESKOM DATA
----------------------------------------------



In this project, 7 functions are created to calculate different metrics for the Eskom data. A brief description of each functions is given below:


1. Metric Dictionary

The metric dictionary function calculates the mean, median, variance, standard deviation, minimum and maximum of a list of items and returns them in the form of a dictionary.

2. Five Number Summary Dictionary

The five number summary function takes a list of items and calculates the minimum, lower quartile, median, upper quartile and maximum and returns them in the form of a dictionary.


3. Date Parser

The function takes a list of strings as input. Each string in the input list is formatted as 'yyyy-mm-dd hh:mm:ss'. The function returns a list of strings where each element in the returned list contains only the date in the 'yyyy-mm-dd' format.

4. Hashtag & Municipality Remover

Takes a pandas dataframe as input. Extract the municipality from a tweet using the given dictionary called ‘ mun_dict’, and insert the result into a new column named 'municipality' in the same dataframe. Use the entry np.nan when a municipality is not found. Extract a list of hashtags from a tweet into a new column named 'hashtags' in the same dataframe. Use the entry np.nan when no hashtags are found.

5. Number of Tweets per Day

takes a pandas dataframe as input. It returns a new dataframe, grouped by day, with the number of tweets for that day. The index of the new dataframe is named Date, and the column of the new dataframe is 'Tweets', corresponding to the date and number of tweets, respectively. The date is formated as yyyy-mm-dd, and is a datetime object.

6. Word Splitter

takes a pandas dataframe as an input. the dataframe contains a column, named 'Tweets'. split the sentences in the 'Tweets' into a list of seperate words, and place the result into a new column named 'Split Tweets'. The resulting words are all lowercase! modify the input dataframe directly. returns the modified dataframe.

7. Stopwords & Link Remover

This function takes a pandas dataframe as input and removes all the stopwords in the input and returns a modified version of the pandas dataframe.




My Package
This library is made to handle the following data inputs: 
- lists
- dataframes


Building this package locally:
'python setup.py sdist'


Installing this package from Github:
'pip install git+https://github.com/teamCEKTA/Eskom_staege_2.git'


Importing from the function package:
from e_Functions_package import efunctions
Then you are set to call whichever function you require in the package


Updating this package from Github
'pip install --upgrade git+https://github.com/teamCEKTA/Eskom_staege_2.git'


Usage
Examples of how to use the functions with their expected output:
1. dictionary_of_metrics(items)
   items = [1, 2, 3, 4, 5, 6]
   expected outcome: {'max': 6.0,
                      'median': 3.5, 
                      'min': 1.0, 
                      'q1': 2.25, 
                      'q3': 4.75}
2. five_num_summary(items)
   items = [1, 2, 3, 4, 5, 6]
   expected outcome: {'max': 6.0, 
                      'median': 3.5, 
                      'min': 1.0, 
                      'q1': 2.25, 
                      'q3': 4.75}
 
3. date_parser(dates)

  dates =  ['2019-11-29 12:50:54','2019-11-29 12:46:53', '2019-11-29 12:46:10']
  expected outcome: ['2019-11-29', '2019-11-29', '2019-11-29']


4. extract_municipality_hashtags(df)

   df = twitter_df
   
   	Tweets	                                                  Date
0	@BongaDlulane Please send an email to mediades...    |2019-11-29 12:50:54

1	@saucy_mamiie Pls log a call on 0860037566	     |2019-11-29 12:46:53

2	@BongaDlulane Query escalated to media desk.	     |2019-11-29 12:46:10

3	Before leaving the office this afternoon, head...    |2019-11-29 12:33:36

4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...    |2019-11-29 12:17:43

expected outcome:

	Tweets	                                            Date	         municipality    hashtags
0	@BongaDlulane Please send an email to mediades... |2019-11-29 12:50:54	|NaN	        |NaN

1	@saucy_mamiie Pls log a call on 0860037566	  |2019-11-29 12:46:53	|NaN	        |NaN

2	@BongaDlulane Query escalated to media desk.	  |2019-11-29 12:46:10	|NaN	        |NaN

3	Before leaving the office this afternoon, head... |2019-11-29 12:33:36	|NaN	        |NaN

4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN... |2019-11-29 12:17:43	|NaN	        |[#eskomfreestate, #mediastatement]

5. number_of_tweets_per_day(df)

df = twitter_df

      Tweets	                                                       		Date
	0	@BongaDlulane Please send an email to mediades...	  |2019-11-29 12:50:54

	1	@saucy_mamiie Pls log a call on 0860037566	          |2019-11-29 12:46:53

	2	@BongaDlulane Query escalated to media desk.	          |2019-11-29 12:46:10

	3	Before leaving the office this afternoon, head...	  |2019-11-29 12:33:36

	4	#ESKOMFREESTATE #MEDIASTATEMENT : ESKOM SUSPEN...	  |2019-11-29 12:17:43

expected outcome:

     Date       	 Tweets
	2019-11-20	|18

	2019-11-21	|11

	2019-11-22	|25

	2019-11-23	|19

	2019-11-24	|14
	

6. word_splitter(df)

df = twitter_df

       Tweets	                                                       		 Date
	0	@BongaDlulane Please send an email to mediades...	  |2019-11-29 12:50:54

	1	@saucy_mamiie Pls log a call on 0860037566	          |2019-11-29 12:46:53


expected output:

	Tweets	                                  	Date	                    Without Stop Words	       Split Tweets
	0	@BongaDlulane Please send an email... |2019-11-29 12:50:54  |[@bongadlulane, send, email,...|[@bongadlulane, please, send,...]

	1	@saucy_mamiie Pls log... 	      |2019-11-29 12:46:53  |[@saucy_mamiie, pls, ...]	    |[@saucy_mamiie, pls, log, a,...]


7.stop_words_remover(df)

df = twitter_df

    Tweets	                                                       		Date
	0	@BongaDlulane Please send an email to mediades...	  |2019-11-29 12:50:54

	1	@saucy_mamiie Pls log a call on 0860037566	          |2019-11-29 12:46:53


expected outcome:

 	Tweets	                                            Date	            Without Stop Words
	0	@BongaDlulane Please send an email to mediades... |2019-11-29 12:50:54	|[@bongadlulane, send, email, mediadesk@eskom.c...]

	1	@saucy_mamiie Pls log a call on 0860037566	  |2019-11-29 12:46:53	|[@saucy_mamiie, pls, log, 0860037566]

Support:
---------

For more information and additional support:
email {amogelang1996@gmail.com,
       eltonmaepa7@gmail.com,
       keithtakarinda@gmail.com,
       mthethwa.charity.khosi@gmail.com,
       tskhungwini@gmail.com}


Authors and acknowledgment
---------------------------

This package was created by 5 aspiring Data Scientists;
Amogelang Mpyatona
Charity Mthethwa
Elton Maepa
Keith Takarinda
Thamsanqa Skungwini

We appreciate the support and help provided to us by the following individuals;
Explore Data Science Academy(EDSA) assistants
Our Supervisor Sicelukwanda Zwane

