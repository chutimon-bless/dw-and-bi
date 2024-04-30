This project utilizes dbt to perform data transformation and uses PostgreSQL as the data warehouse.

### create and activate virtual environment
```python
python -m venv ENV
source ENV/bin/activate
```

### install essential libraries
```python
pip install dbt-core dbt-postgres
```

### initialize the project
```
dbt init
```

### set up your profile 
      dbname: postgres
      host: localhost
      pass: postgres
      port: 5432
      schema: public
      threads: 1
      type: postgres
      user: postgres

### check connection with PostgreSQL
```
cd DS525
dbt debug
```

### run dbt
```
dbt run
```
