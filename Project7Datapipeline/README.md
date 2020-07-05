The purpose of this week's project was to build a data pipeline consisting of reading out specific tweets based on a filter from the twitter API stream listener. This extensive pipeline is facilitated by docker. The general outline of these steps are as follows:

1. extract the necessary dictionaries from each tweets json file using the twitter stream listener using a specified filter, in this case any tweet in english and mentioning Berlin
2. import all this into a mongo data base, keeping only the desired info
3. retrieving these dictionary items from mongo database, calculating each tweets' sentiment score and taking this (along with the info from mongo database) and transferring it to a postgres database
4. execute specific queries based on a defined time period and have them printed into a channel on slack using a slack bot

All these steps should be successful with the DockerCompile directory and all its contents on any operating system having docker. Further detail on the role each container plays in the data pipeline can be found in README files within each container directory.

As an example what the final result may look like:

![botScreenShot](https://user-images.githubusercontent.com/52377705/86530400-b64d4a80-beb8-11ea-835f-079860cfad61.png)
