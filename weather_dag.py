from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from fetch_data import fetch_weather_data

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "start_date": datetime(2025, 3, 2),
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    'weather_dag',
    default_args = default_args,
    schedule_interval = timedelta(minutes = 2),
    catchup = False
):
    fetch_and_store_weather_data = PythonOperator(
        task_id = 'fetch_and_store_weather_data',
        python_callable = fetch_weather_data
    )

fetch_and_store_weather_data