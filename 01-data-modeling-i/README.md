# Instruction

## establish docker configurations via docker-compose.yml file
docker-compose up

## create tables (actors, repo, events)
python create_tables.py

## ETL from json files in folder 'data'
python etl.py