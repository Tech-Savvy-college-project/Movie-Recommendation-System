
# Deploy Backend 


```
git clone https://github.com/David-Thapa/Movie-Recommendation.git
cd Movie-Recommendation/backend
pipenv shell
pipenv install -r requirements.txt
python manage.py runserver
```

## insert your credentials in `.env` file as template is provided in './env-template' file 


# Load DB

### First create database using command as below

```
λ mysql -u root -p 
Enter password: 
Welcome to the MariaDB monitor.  Commands end with ; or \g.
...

MariaDB [(none)]> create database movies_db;

```

### then migrate the django models to db
```
python manage.py makemigrations
python manage.py migrate
```

### then load data with below commands 
```
cd db_docs
mysql <db_username> -p < load.sql
        eg: msyql root -p < load.sql
```