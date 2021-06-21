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
$ pipenv run python craft key --store
```

edit `.env` file

```
KEY=your-key

DB_CONNECTION=sqlite
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=masonite.db
DB_USERNAME=root
DB_PASSWORD=root
```

```
$ pipenv run python craft migrate
```

```
$ npm install
```

compile
```
$ npm run dev
```

### run

run server
```
$ pipenv run python craft serve
```

demo: http://localhost:8000
