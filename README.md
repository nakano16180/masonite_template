## Masonite template

[demo](https://masonite-app.herokuapp.com/)

### install

```
$ cd masonite_template/
$ pipenv install
$ pipenv run craft install
```

### setup for local (use sqlite)
generate key

```
$ pipenv run craft key
```

edit `.env` file

```
KEY=your-key

DB_CONNECTION=sqlite
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=blog.db
DB_USERNAME=root
DB_PASSWORD=root
```

```
$ pipenv run craft migrate
```

### use postgresql for database

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
KEY=<your-secret-key>

DB_CONNECTION=postgres
DB_HOST=localhost
DB_PORT=5432
DB_DATABASE=hello_masonite_dev
DB_USERNAME=postgres
DB_PASSWORD=postgres
DB_LOG=True

```

```
$ pipenv run craft migrate
```

### run

```
$ pipenv run craft serve
```

### use tailwindcss

```
$ npm install
```

compile
```
$ npm run dev
```

run server
```
$ pipenv run craft serve
```