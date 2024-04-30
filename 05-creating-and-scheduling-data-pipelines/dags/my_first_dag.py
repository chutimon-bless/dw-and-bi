from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.utils import timezone

with DAG(
    # required parameters: id, param, schedule
    "my_first_dag",
    start_date=timezone.datetime(2024,3,23), # datetime obj
    schedule=None, # run when triggered manually
    tags=["DS525"], # ใส่ tag จะได้หาง่ายๆ
):
    # create task with emptyoperator
    my_first_task = EmptyOperator(task_id="my_first_task")
    my_second_task = EmptyOperator(task_id="my_second_task")

    # establish dependencies (direct the sequence)
    my_first_task >> my_second_task