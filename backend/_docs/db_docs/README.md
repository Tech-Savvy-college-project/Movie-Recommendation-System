

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




# schema of `movies_movie` table of `movies_db`

```
+-------------------+--------------+------+-----+---------+-------+
| Field             | Type         | Null | Key | Default | Extra |
+-------------------+--------------+------+-----+---------+-------+
| tmdb_id           | varchar(20)  | NO   | PRI | NULL    |       |
| imdb_id           | varchar(50)  | NO   |     | NULL    |       |
| original_language | varchar(255) | NO   |     | NULL    |       |
| original_title    | varchar(255) | NO   |     | NULL    |       |
| runtime           | int(11)      | NO   |     | NULL    |       |
+-------------------+--------------+------+-----+---------+-------+
```




# schema of users_user

```

MariaDB [new_db]> describe users_user;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | bigint(20)   | NO   | PRI | NULL    | auto_increment |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| first_name   | varchar(150) | NO   |     | NULL    |                |
| last_name    | varchar(150) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| date_joined  | datetime(6)  | NO   |     | NULL    |                |
| name         | varchar(255) | NO   |     | NULL    |                |
| email        | varchar(255) | NO   | UNI | NULL    |                |
| password     | varchar(255) | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
11 rows in set (0.000 sec)
```