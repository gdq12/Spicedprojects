This repository consists of files needed to create and run the tweepy container, a container that collects filtered tweets from twitters streaming API. It consists of the following files:

1. Docker file
  - installs python 3.6-slim into container by downloading parent image from docker hub
  - creates a working directory (tweets) in the container where all necessary files will be copied to
  - copies into the /tweets directory the config, get_tweets and requirements files
  - installs the listed python libraries in the container
  - instructions that upon container initiation, it will run python and then the get_tweet script

2. requirements.txt
  - text file consisting of a list of python libraries to be installed upon container building: tweepy, pymongo, DateTime
  - this will be used by the Dockerfile when the container is being built

3. config.py
  - consists of confidential twitter credentials for acquiring a twitter authenitication token
  - the credentials were kindly provided by one of the Spiced Academy instructors
  - it called upon by the get_tweety.py when executed

4. get_tweets.py
  - runs a streamlistener on the twitter streaming API and collects tweet jsons based on streamlistener filter.
  - general outline of script:
    - simultaneously creates a connection variable to the mongo database container and creates the twitter database along with the tweets collection within that database
    - creates an authentication token function based on the credential info provided by config.py, when called upon.
    - creates a streamlistener function. When called upon it grabs the whole tweet in json format, extracts the: user, username, location, text, hashtags, time tweet was made and time when tweepy picked up the tweet. It then takes these specific key/values and saves it into a new dictionary object and then transfers this to the tweets collection of the twitter database in the mongo container. Within this same function, it overcomes twitters api ratelimit by disconnecting from the stream when error 420 is applied onto it by twitter and keeps the container running for 6 minutes while waiting for the streamlistener to regain permission to stream for more tweets.
    - creates a stream variable using the token authentication and streamlistener and filter for tweets based on a key word and english language parameters
    - a 3 second delay is instilled within the script to create a small delay between each tweet collection loop

Helpful terminal commands for project revisitation:

Running container independent of docker compose:
- docker build -t containerName .
  - create an image for container named tweet_collector with Dockerfile in current directory
- docker run -it -d containerName
  - to launch a container and print out the tweets in the terminal (w/0 -d) or run in the background (w/ -d)
- control + c
  - to stop image form running
- docker start -i containerName
  - to restart a container
  - use docker ps -a to look up the container name
- docker run -it imageID
  - to restart a container based on image
  - to get image id use docker images
