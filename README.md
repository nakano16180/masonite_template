## Masonite template

[demo](https://masonite-app.herokuapp.com/)

### install

```
$ cd masonite_template/
$ pipenv install -r requirements.txt
```

### setup database

```
$ docker run -v /var/lib/psql --name psql_data busybox
$ docker run --volumes-from psql_data --name psql -p 5432:5432 -e POSTGRES_PASSWORD=postgres -d postgres:9.6
```

```
$ docker exec -it psql bash
# psql -h localhost -U postgres

postgres=# create database hello_masonite_dev;
postgres=# \q

# exit
```

edit .env

```
DB_CONNECTION=postgres
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=hello_masonite_dev
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_LOG=True

```

### run

```
$ craft migrate
```

```
$ craft serve
```