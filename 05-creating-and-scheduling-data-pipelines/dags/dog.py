import logging

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils import timezone

import requests
import json

def _get_dog_api():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    data = response.json()
    logging.info(data)
    with open("/opt/airflow/dags/dog.json","w") as f:
        json.dump(data,f)
        

with DAG(
    # required parameters: id, param, schedule
    "dog", # id 
    start_date=timezone.datetime(2024,3,23), # datetime obj
    schedule="@daily", # run every minute (cron expression)
    tags=["DS525"], # ใส่ tag จะได้หาง่ายๆ
):
    # create task with emptyoperator
    start = EmptyOperator(task_id="start")

    get_dog_api = PythonOperator(
        task_id="get_dog_api",
        python_callable=_get_dog_api, # รับชื่อ function ไ่ม่ต้องมี () 
    )

    end = EmptyOperator(task_id="end")


    # establish dependencies (direct the sequence)
    start >> get_dog_api >> end