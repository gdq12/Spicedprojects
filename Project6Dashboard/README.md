The purpose of this week's project was to build a dashboard that summarizes the fictional Northwind Database originally created by microsoft for sql training. The data was kindly cleaned up by a Spiced Academy (Berlin) instructor and can be retrieved [here](https://github.com/pawlodkowski/northwind_data_clean). The sql commands used to import the csv files into the cloud local machine/amazon RDS cloud along with creating join tables for analysis can be found in the sqlCommands subrepo of this repository. The metabase dashboard built for this project is in an Amazon EC2 cloud machine that will soon be shut down, but the tables from which the graphs in the dashboard were produced can be found in the tablesMetbase subrepo here. Should one like to regenerate the metabase dashboard in their own cloud machine, the db files are here to be used for that. A glimpse of the dashboard is provided by the following gif:

![dashboardGIF]

Relative info:
- used PostgresSQL for executing SQL queries. Used mac customized [app](https://postgresapp.com/)
- used [Postico](https://eggerapps.at/postico/) for facilitating databases in local machine and amazon RDS cloud
- csv file for country abbreviations/latitude/longitude can be found [here](https://www.kaggle.com/eidanch/counties-geographic-coordinates)
