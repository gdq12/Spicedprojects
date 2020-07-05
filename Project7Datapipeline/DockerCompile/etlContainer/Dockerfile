#uses an image from docker hub for installing python into container
FROM python:3.6-slim

# the working directory where all necessary files will be copied into the container
WORKDIR /etlJob

# to copy the requirements.txt and etl.py files into the container working directory
COPY . /etlJob

# install libraries indicated by requirements.txt
RUN pip install --trusted-host pypi..org -r requirements.txt

# first start python and then run etl.py once container is initiated
CMD ["python", "etl.py"]
