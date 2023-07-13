# Akkodis Technical Test Setup:

- Install MySql/MariaDB server

- Install Python (3.10.1 or higher recommended)

- Create a virtual environment and activate it
```shell
$ python -m venv venv
```
```shell
$ source venv/bin/activate # Linux
```
```shell
> .\venv\bin\activate # Windows
```

- Install dependencies
```shell
$ cd src
$ pip install -r requirements.txt
```

- Create a database and a user with permissions to access it

- Create a .env file in the root of the project with the following content:
```
DB_HOST=<database host>
DB_PORT=<database port>
DB_NAME=<database name>
DB_USER=<database user>
DB_PASSWORD=<database password>
```
There is a .env.example file with sample data.

- Run the migrations
```shell
$ alembic upgrade head
```

- Run the application
```shell
$ python main.py
```


- Get the documentation at http://localhost:5000/ui

- Run the tests
```shell
$ pytest tests
```
