Cloud Data Warehouse

Sparkify Analytics

As the trend of custom recommended playlist increases. We are startup group who wants to fullfil their customers needs to provide enhanced and best recommended music playlist according to their mood and category for our customers via music streaming app.

The process started when we started to analyze our users activity, to know them better what kind of songs they listen and construct a real time ETL Workflow, which will parse, analyze, aggregate and Insert data into Postgres Database which will help us in categorizing and enhancing our recommendation models for our customer.

Project Description:

For this project, we have hosted our data warehouse on cloud using AWS Redshift as a service. We have stored our log_data and event_data files on S3.
The ETL pipeline is build as follows:
1) Fetch data from S3 and store it as dataframe.
2) Create and populate two staging tables from the dataframe.
3) Create and populate the remaining facts and dimensions table.

Schema for staging tables:

The log_data directory contains events files in JSON format. Using the same schema we have created staging_events staging table as follows: 
Table: staging_events

    artist          VARCHAR,
    auth            VARCHAR, 
    firstName       VARCHAR,
    gender          VARCHAR,   
    itemInSession   INTEGER,
    lastName        VARCHAR,
    length          FLOAT,
    level           VARCHAR, 
    location        VARCHAR,
    method          VARCHAR,
    page            VARCHAR,
    registration    BIGINT,
    sessionId       INTEGER,
    song            VARCHAR,
    status          INTEGER,
    ts              TIMESTAMP,
    userAgent       VARCHAR,
    userId          INTEGER

The log_data directory contains log files in JSON format. Using the same schema we have created staging_songs staging table as follows: 
Table: staging_songs

    song_id            VARCHAR,
    num_songs          INTEGER,
    title              VARCHAR,
    artist_name        VARCHAR,
    artist_latitude    FLOAT,
    year               INTEGER,
    duration           FLOAT,
    artist_id          VARCHAR,
    artist_longitude   FLOAT,
    artist_location    VARCHAR


We have distributed our tables in form of STAR schema, for better analysis. The list of tables and their fields are as follows:

Fact Table, also known as songplays table will contain records from log data associated with the songs such as:

    songplay_id INTEGER IDENTITY(0,1) PRIMARY KEY,
    start_time  TIMESTAMP NOT NULL sortkey distkey,
    user_id     INTEGER,
    level       VARCHAR,
    song_id     VARCHAR NOT NULL,
    artist_id   VARCHAR NOT NULL,
    session_id  INTEGER,
    location    VARCHAR,
    user_agent  VARCHAR

Dimension Tables design have been categorized as follows:

1) Users Table - To get all the users from music streaming app, the respective schema for the table is attached below
    
    user_id     INTEGER NOT NULL PRIMARY KEY sortkey,
    first_name  VARCHAR NOT NULL,
    last_name   VARCHAR NOT NULL,
    gender      VARCHAR NOT NULL,
    level       VARCHAR NOT NULL
    
2) Songs Table - Collections of songs from music database, the respective schema for the table is attached below
    
    song_id    VARCHAR PRIMARY KEY sortkey,
    title      VARCHAR NOT NULL,
    artist_id  VARCHAR NOT NULL,
    year       INTEGER NOT NULL,
    duration   FLOAT

3) Artist Table - Collections of artists from music database, the respective schema for the table is attached below
    
    artist_id VARCHAR PRIMARY KEY sortkey,
    name VARCHAR,
    location VARCHAR,
    lattitude FLOAT,
    longitude FLOAT

4) Time Table - Timestamps of song records played by the user which partitioned by year, month,.etc, the respective schema for the table is attached below
    
    start_time TIMESTAMP PRIMARY KEY distkey sortkey,
    hour INTEGER NOT NULL,
    day INTEGER NOT NULL,
    week INTEGER NOT NULL,
    month INTEGER NOT NULL,
    year INTEGER NOT NULL,
    weekday INTEGER NOT NULL
    

The Project Structure is as follows:

Data: For this project the data is uploaded on AWS S3. The directory for the where song_data and log_data JSOn file resides.
sql_queries.py - contains all the sql queries which is utilized in create_tables.py and etl.py python files.
create_tables.py -  This file contains python code to drop tables, create tables and insert records into the database and tables.
etl.py - This file contains python code to insert data from the staging tables into different tables and finally populating the songplays table.
Test_Notebook.ipynb - It is a python notebooks used to perform tests on the ingested data, to maintain data integrity.

Project Steps:

1) Write sql queries for create, insert and drop tables into sql_queries.py file and save it.
2) Open console and run create_tables.py file, it will drop exisiting tables, create new tables for the project.
3) Open etl.ipynb notebook and execute step by step to ingest one file of song_data and log_data into database and tables.
4) Open etl.py file and edit as per etl.ipynb step by step to ingest all the data into database and tables.
5) Open console and run etl.py file to ingest data into database and tables.
6) Run test.ipynb to check the results and data integrity.

ETL Pipeline Flow:

1) First open a new configuration file and write redshift connection configuration into the file
2) Read the configuration file and create redshift cluster using python libraries boto3 which is an AWS SDK for python
3) After creating the cluster, check the connection as well as test the connection to database.
4) Edit sql_queries.py file and write SQL statements to drop, create, copy and insert to load data into respective tables.
5) After editing the sql_queries.py file, run create_tables.py from console and it will create tables as per statements.
6) Check into redshift whether tables have been created or not.
7) Run etl.py file to copy data from s3 and populate all the tables as per insert statements, written into sql_queries.py file
8) Perform queries on Redshift or from juypter notebook to check the counts of ingested data.


Note: Before running etl.py or Test_Notebook.ipynb, make sure to edit sql_queries.py file if needed and run create_tables.py file to drop and create new tables.

Author: Devansh Modi