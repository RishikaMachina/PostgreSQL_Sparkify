# DROP TABLES

songplay_table_drop = "drop table if exists songplay_table"
user_table_drop = "drop table if exists user_table"
song_table_drop = "drop table if exists song_table"
artist_table_drop = "drop table if exists artist_table"
time_table_drop = "drop table if exists time_table"

# CREATE TABLES

songplay_table_create = ("""
create table if not exists songplay_table(
    songplay_id serial primary key, 
    start_time bigint not null, 
    user_id int not null, 
    level text, 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location text, 
    user_agent text)
""")

user_table_create = ("""
create table if not exists user_table(
    user_id int primary key, 
    first_name text, 
    last_name text, 
    gender varchar, 
    level varchar)
""")

song_table_create = ("""
create table if not exists song_table(
    song_id text primary key, 
    title text, 
    artist_id text not null, 
    year int, 
    duration float)
""")

artist_table_create = ("""
create table if not exists artist_table(
    artist_id text primary key, 
    name text not null, 
    location text, 
    latitude numeric, 
    longitude numeric)
""")

time_table_create = ("""
create table if not exists time_table(
    start_time bigint primary key, 
    hour text, 
    day int not null, 
    week text, 
    month int not null, 
    year int not null, 
    weekday int)
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplay_table (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)
                VALUES (DEFAULT, %s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO  user_table(user_id, first_name, last_name, gender, level) 
    VALUES ( %s, %s, %s, %s, %s)
    ON CONFLICT(user_id) 
    DO UPDATE SET level = excluded.level;
""")

song_table_insert = ("""
INSERT INTO song_table(song_id, title, artist_id, year, duration) 
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (song_id) DO NOTHING;
""")

artist_table_insert = ("""
INSERT INTO artist_table(artist_id, name, location, latitude, longitude)
    VALUES (%s, %s, %s, %s, %s)
    ON CONFLICT (artist_id) DO NOTHING;
""")


time_table_insert = ("""
INSERT INTO time_table(start_time, hour, day, week, month, year, weekday)
    VALUES ( %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time) DO NOTHING;
""")

# FIND SONGS

song_select = ("""
select song_table.song_id, artist_table.artist_id from song_table 
            join artist_table on artist_table.artist_id = song_table.artist_id
            where song_table.title = %s and artist_table.name = %s and song_table.duration = %s;
""")


# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]