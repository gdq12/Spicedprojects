Principle objective of this project is to build a dockerized Data Pipeline that analyzes tweet sentiments and send them to slackbot for hourly reporting. The pipeline is executed and facilitated via Docker-Compose, a tool used to build and run multiple containers in an "orchestrated" sequential format. This is executed via a docker-compose.yaml in 1 directory above each of the container subdirectory folders. This yaml file consists of instructions for building each container in the pipeline, whether it maybe going into each sub directory to execute a respective docker file and build the container from scratch, or downloading an image from docker hub to build a container based on a prebuilt container provided by the docker community. The following is a brief description of each container and their principle role in the pipeline. More details about each respective container can be found in their respective sub repos.

- Tweepy: connects to twitter streaming api to read and collected filtered incoming tweets
- Mongo Database: receives and stores the json format tweets within its collection.
- ETL: container that extracts tweet info from the mongo database, calculates the sentiment factor of each tweet and transforms it to postgres friendly format and then loads it into a postgres table within its database.
- Postgres
- Slack Bot


Commands for terminal:
a. docker-compose build
- builds the containers based on the Dockerfiles in each sub repo
- command must be executed in terminal where the docker-compose.yaml file is
b. docker-compose up
- to initiate the pipeline and all containers in specified sequence (based on all container configurations)
c. docker exec -it dockercompile_my_mongodb_1 mongo
- once mongodb container up and running, enter container to check on collections
d. show dbs
- prints list of dbs in mongo, verify that twitter is in the list
c. use twitter
- to enter twitter db
e. show collections
- prints list of collections in db, should see tweets the only on_error
f. db.tweets.find()
- prints out all the entries (tweet dictionaries) of the tweet collection in the terminal
g. db.tweets.count()
- prints out the current number of entries in the tweets collection
h. control + c
- to leave the mongodb container
i. docker exec -it dockercompile_my_postgresdb_1 psql -U postgres
- to enter the postgresdb container once its up and running
j. \l
- once inside postgres, prints the list of dbs
k. \c postgres
- to enter the postgres db
l. \dt
- prints a list of all the tables in the db, should see tweetpostgres as the only one
m. select * from tweetpostgres;
- prints out all the current rows in the tweetpostgres table
n. select count(\*) from tweetpostgres;
- prints out the total number of rows in the tweetpostgres table
o. control + d
- to leave the postgres container
p. docker start dockercompile_my_mongodb_1/dockercompile_my_postgresdb_1
- to start the containers after the pipeline has been closed
q. docker exec -it dockercompile_my_mongodb_1 mongo/dockercompile_my_postgres_1 psql -U postgres
- to re-enter container after its been restarted
- also with postgres, can just start container only and play around with table in postico rather than in terminal

To check postgres db via postico:
- nickname: dataPipeline
- Host: localhost
- Port: 5555
- User: postgres
- password: xxxx
- database: postgres
