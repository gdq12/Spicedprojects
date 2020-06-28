The purpose of this week's project was to build a dashboard that summarizes the fictional Northwind Database originally created by microsoft and introduce oneself to sql. The data was kindly cleaned up by a Spiced Academy (Berlin) instructor and can be retrieved [here](https://github.com/pawlodkowski/northwind_data_clean). The sql commands used to import the csv files into the local machine/amazon RDS cloud along with creating join tables for analysis can be found in the sqlCommands subrepo of this repository. The metabase dashboard built for this project is in an [Amazon EC2 cloud machine](http://18.196.47.181/public/dashboard/42b26f56-5f3e-4532-83b9-01d88409b43b) that will soon be shut down, but the tables from which the graphs in the dashboard were produced can be found in the tablesMetbase subrepo here. Should one like to regenerate the metabase dashboard in their own cloud machine, the db files are here available here (metabase.db.mv.db and metabase.db.trace.db). A glimpse of the dashboard is provided by the following gif:

![dashboardGIF](https://github.com/spicedacademy/allspice-arrays-code/blob/gloria/Project6Dashboard/NorthwindDashboard.gif)

General points on Northwind data:
- The majority of the revenue for this company comes from the United States and Germany, with the majority products exported to these countries being: dairy, confections and poultry.
- The countries that this company exports to are Argentina, Spain, Portugal, Norway and Poland.
- They company receives the largest revenue from orders that get shipped out 1-10 days from the order date.
- When comparing an employee's hiring age to hiring date and their impact and the amount of revenue they produced for the company, hiring date appears to play a greater role in their total revenues.
- In examining the discounts each employee gave customers to their sales, it appears to play a small role in their total revenue since the variation of average discount and total revenue for each employee don't coincide.
- In comparing product stock continuation vs discontinuation, products within the $100-$150 unit price range were all discontinued, while those in other ranges were largely not. 

Relative info:
- used PostgresSQL for executing SQL queries. Used mac customized [app](https://postgresapp.com/)
- used [Postico](https://eggerapps.at/postico/) for facilitating databases in local machine and amazon RDS cloud
- csv file for country abbreviations/latitude/longitude can be found [here](https://www.kaggle.com/eidanch/counties-geographic-coordinates)
