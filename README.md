# Data modeling - PostgreSQL

The purpose of the project is to model song & log files data [http://millionsongdataset.com] into a SQL database - PostgreSQL. The modeled data can be used for analytics purposes.


## **Overview**

### 1. Schema - Star schema

Fact table           - Songplay_table
Dimension tables     - user_table, artist_table, time_table, song_table

### 2. Tables attributes datatypes

#### Songplay table

- songplay_id --> Auto increment primary key
- start_time  --> big int
- user_id     --> int
- level       --> text
- song_id     --> text
- artist_id   --> text
- session_id  --> int
- location    --> text
- user_agent  --> text


#### User table 

- user_id     --> int
- first_name  --> text
- last_name   --> text
- gender      --> text
- level       --> text


#### Song table

- song_id     --> text
- title       --> text
- artist_id   --> text
- year        --> int
- duration    --> float


#### Artist table

- artist_id   --> text
- name        --> text
- location    --> text
- latitude    --> numeric
- longitude   --> numeric


#### Time table

- start_time  --> big int
- hour        --> text
- day         --> int
- week        --> text
- month       --> int
- year        --> int
- weekday     --> int

### 3. ETL pipeline

The pipeline uses multiple functions to convert data from json to pandas dataframe and then add to their respective columns of fact and diomension tables.

### 4. Example queries

- Get all unique users in Sparkify accounts
    <p> select unique(user_id) from user_table; </p>

- Get all unique artists in Spariky databases
    <p> select unique(artist_name) from artist_table; </p>

- Number of albums per artist available on Spariky 
    <p> select count(title) from song_table group by artist_id; </p>
