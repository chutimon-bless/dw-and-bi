import logging

from airflow import DAG
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils import timezone

def _say_hello():
    logging.debug("This is debug log")
    logging.info("hello")

with DAG(
    # required parameters: id, param, schedule
    "hello",
    start_date=timezone.datetime(2024,3,23), # datetime obj
    schedule=None, # run when triggered manually
    tags=["DS525"], # ใส่ tag จะได้หาง่ายๆ
):
    # create task with emptyoperator
    start = EmptyOperator(task_id="start")

    echo_hello = BashOperator(
        task_id="echo_hello",
        bash_command="echo 'hELLo'"
        )

    say_hello = PythonOperator(
        task_id="say_hello",
        python_callable=_say_hello, # รับชื่อ function ไ่ม่ต้องมี () 

    )

    end = EmptyOperator(task_id="end")


    # establish dependencies (direct the sequence)
    start >> echo_hello >> end
    start >> say_hello >> end