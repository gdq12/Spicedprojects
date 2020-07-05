This repository consists of files needed to create and run the slack bot container, a container that executes specific queries of the tweetpostgres table in the postgres database container, formats the resulting queries and has them printed out in a slack channel via a slack robot app. It consists of the following files:

1. Docker file
  - installs python 3.6-slim into container by downloading parent image from docker hub
  - creates a working directory (slacky) in the container where all necessary files will be copied to
  - copies into the /slacky directory the slack_bot and requirements files
  - installs the listed python libraries in the container
  - instructions that upon container initiation, it will run python and then the slack_bot script

2. requirements.txt
  - text file consisting of a list of python libraries to be installed upon container building: slackclient, sqlalchemy, datetime, psycopg2-binary
  - this will be used by the Dockerfile when the container is being built

3. config.py
  - consists of authenitication token for the slack bot
  - it called upon by the slack_bot.py when executed

4. slack_bot.py
  - execute certain queries in the postgres database from the tweetpostgres table, saves/reformats them and then sends them to the slack robot for the results to be printed in slack
  - general outline of the script:
    - creates a variable to connect to the postgres database container
    - creates a variable to connect to the slack bot
    - saves the starting timestamp of the while loop as time1
    - pauses the while loop for 1 hour
    - saves the time timestamp of the post pause as time2
    - executes a function that acquires results from the following queries (with specified time frame time1 to time2) and saves them as string format: total number of tweets, total number of retweets, number of tweets geo-tagged to Berlin, number of tweets geo-tagged to Germany, counts number of users that tweeted more than once, counts the number of #Berlin, the tweet with the highest sentiment value and the tweet with the lowest sentiment value
    - prints these results via the slack bot authentication on the #random channel
