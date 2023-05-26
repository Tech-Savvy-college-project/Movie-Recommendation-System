
use movies_db;
load data infile 'movies.csv' into table movies_movie fields terminated by ','  enclosed by '"' lines terminated by '\n' ignore 1 rows ;

