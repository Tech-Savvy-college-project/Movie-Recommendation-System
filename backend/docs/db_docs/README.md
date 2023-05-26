

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
