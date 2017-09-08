
# Get Tweets Programatically with R
A project written in R to get tweets. Due to the change of twitter API we can only get tweets within a given period. Usually the last 7 days.

## Prerequisites
This package assumes using RStudio. Please go ahead and download RStudio at https://www.rstudio.com/

## Components
- **Tweet:** Model class to give some informations about a specific tweet.
  -text	
  
  -favorited	
  
  -favoriteCount	
  
  -replyToSN	
  
  -created	
  
  -truncated	
  
  -replyToSID	
  
  -id	
  
  -replyToUID	
  
  -statusSource	
  
  -screenName	
  
  -retweetCount	
  
  -isRetweet	
  
  -retweeted	
  
  -longitude	
  
  -latitude


- **Usage:** 
 searchTwitter(searchString, n=25, lang=NULL, since=NULL, until=NULL, locale=NULL, geocode=NULL, sinceID=NULL, maxID=NULL,
	      resultType=NULL, retryOnRateLimit=120, ...).
	      
For more information how to use this library. Please visit: https://www.rdocumentation.org/packages/twitteR/versions/1.1.9/topics/searchTwitter

- **Exporter:** Export tweets to a csv file named "TwitterData.csv".
Use command: > write.csv(tweets, "TwitterData.csv")

## Examples of R usage in our project
- Install library
``` R
>install.packages('TweeteR')
> require('TweeteR')
```    
- Setup authentication
``` R
>setup_twitter_oauth(consumer_key,consume_secret,access_key,access_secret) 
#These paramenters retrieved from http://apps.twitter.com
	  
```    
- Querry tweets
``` R
>tweets <- searchTwitter('Tropical Depression Harvey', n=10000, lang='en', since='2017-08-26', until='2017-09-08')
>tweetds <-twListToDF(tweets) #Convert data to data frame
>write.csv(tweetds, "TwitterData.csv") # export data frame to csv file
```
!Hura
