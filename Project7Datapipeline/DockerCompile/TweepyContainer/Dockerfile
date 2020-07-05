# bring in a parent image from docker hub to install python-have to test to see if works well
FROM python:3.6-slim

# create working directory
WORKDIR /tweets

# copy the requirements.txt file (for installing necessary python libraries), config.py (twitter credentials for twitter token), get_tweets.py (for tweet collection via streamlistener)
COPY . /tweets

# install libraries specified in requirements.txt fie
RUN pip install --trusted-host pypi.python.org -r requirements.txt

#run python and get_tweet script when the container is launched
CMD ["python", "get_tweets.py"]
