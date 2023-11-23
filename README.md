# excel/csv-2-SQL

A simple python script for migrating excel tables or csv files to an SQL database
using pandas.

Put all the .xlsx/.xls/.csv files in the 'excel-or-csv-files' folder and pass the path to that folder in the script.
Compile all the db connection parameters and run the script.

There is a small docker compose for creating a postgres db and a simple grafana instance.
For using grafana is necessary to login in the gui at localhost:3000 with the default credentials ( user = admin, password = admin), to connect to de dockerized db inside grafana add a postgres datasource (as host you have to use the container name) and connect.
From grafana is then possible to make queries and visualize data