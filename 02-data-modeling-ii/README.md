## Project description
This project aims to extract data from github events JSON files and load into a NoSQL database, specifically using Apache Cassandra in this case.

## Instruction

### establish docker configurations via docker-compose.yml file
```
docker-compose up
```

### create a virtual environment for installing packages with versions pinned in requirements.txt
```
python -m venv ENV
source ENV/bin/activate  
pip install -r requirements.txt
```

### create keyspaces and ETL
```
python etl.py
```