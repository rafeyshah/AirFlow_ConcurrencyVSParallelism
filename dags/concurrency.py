"""
Code that goes along with the Airflow located at:
http://airflow.readthedocs.org/en/latest/tutorial.html
"""
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator


default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2021, 7, 28),
    "email": ["airflow@airflow.com"],
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
}

dag = DAG("concurrency", default_args=default_args, schedule_interval=timedelta(hours = 1), catchup =False)

t1 = BashOperator(
    task_id='Task_1',
    bash_command='echo 1',
    task_concurrency=2,
    dag=dag
)

t2 = BashOperator(
    task_id='Task_2',
    bash_command='echo 2',dag=dag
)

t3 = BashOperator(
    task_id='Task_3',
    bash_command='echo 3',dag=dag
)
t1>>[t2,t3]