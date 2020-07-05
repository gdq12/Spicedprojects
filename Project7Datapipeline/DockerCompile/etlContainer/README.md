This repository consists of files needed to create and run the ETL container, a container that retrieves tweet dictionaries from the mongo database tweets collection, modies the dictionary by adding the calculated sentiment factor to it, and inserting this into the postgres database container. It consists of the following files:

1. Docker file
  - installs python 3.6-slim into container by downloading parent image from docker hub
  - creates a working directory (tweets) in the container where all necessary files will be copied to
  - copies into the /tweets directory the etl and requirements files
  - installs the listed python libraries in the container
  - instructions that upon container initiation, it will run python and then the etl script

2. requirements.txt
  - text file consisting of a list of python libraries to be installed upon container building: pymongo, SQLAlchemy, psycopg2-binary, vaderSentiment
  - this will be used by the Dockerfile when the container is being built

3. etl.py
  - extracts tweet dictionaries from the tweet collection, calculates the sentiment factor of each tweet, adds this back into the dictionary variable and then adds it to a postgres table in the postgres container
  - general outline of the script:
    - creates a variable to connect to the mongo database container
    - creates a variables to connect to the postgres database container
    - creates a new table query for the postgres database container and executes it
    - saves the starting timestamp of the while loop as time1
    - pauses the while loop for 90 seconds
    - saves the time timestamp of the post pause as time2
    - connects to the mongo database container and extracts the tweet dictionary based on those tweets with timestamps between time1 and time2
    - takes the text key/value from the tweet dictionary, calculate the sentiment factor of the text and inserts this value back into the tweet dictionary
    - creates an insert values into table query and then executes this with the postgres database container connection
