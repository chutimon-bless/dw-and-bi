## Project description
This project aims to create a data pipeline using Apache Airflow.

## Instruction

The docker-compose.yaml file was fetched from airflow.apache.org and edited to reduce resource usage. 

### create essential folders
```
mkdir -p ./dags ./logs ./plugins ./config
echo -e "AIRFLOW_UID=$(id -u)" > .env
```

### run docker compose up
```
docker compose up
```

### create the pipeline by utilizing airflow's DAG and save it as .py file in the dag folder