

command to convert the dbsqlite to mysql database 

```
java -jar client-0.0.5.jar convert --output-format=mysql ~/projects/Movie_recommendation_system/db.sqlite3 .

Source: https://www.rebasedata.com/convert-sqlite-to-mysql-online
```



```
select movie_id, original_language, original_title, popularity, release_date, vote_average, vote_count, revenue, runtime from movie_movies limit 20;
```


# load data from csv file to mariaDB

```

LOAD DATA INFILE 'Movies.csv' INTO TABLE movies_movies FIELDS TERMINATED BY ',' LINES TERMINATED BY '\n' IGNORE 1 ROWS;
```



# load file 

drop database movies_db;
create database movies_db;

```
load data infile 'movies.csv' into table movies_movie fields terminated by ','  enclosed by '"' lines terminated by '\n' ignore 1 rows ;
```